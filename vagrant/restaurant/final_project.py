from flask import Flask,render_template,url_for,request,redirect,flash,jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base,Restaurant,MenuItem

# New imports for the login implementation
from flask import session as login_session
import random,string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)


CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Restaurant Menu Application"


#Create a DB connection and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create a state token to prevent request forgery.
# Store it in the session for latter validation.
@app.route('/login')
def showLogin():
	# Random string or rather salt 
	state = ''.join(random.choice(string.letters) for x in xrange(32))
	login_session['state']=state
	#return "the current state is %s" % login_session['state']
	return render_template('login.html',STATE=state)

@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 160px; height: 160px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output

# DISCONNECT - Revoke a current user's token and reset their login_session

@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print 'Access Token is None'
        response = make_response(json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: '
    print login_session['username']
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response

# Making an API endpoint for Restaurant List(GET Request)
@app.route('/restaurant/JSON')
def restaurantsJSON():
	restaurants = session.query(Restaurant).all()
	listRestaurant=[]
	j=0
	for i in restaurants:
		if i.serializeRestaurant !=[]:
			listRestaurant.append(i.serializeRestaurant)
		j=j+1
	return jsonify(Restaurants=listRestaurant)

# Making an API endpoint for Restaurant Menu(GET Request)
@app.route('/restaurant/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	menuItems = session.query(MenuItem).filter_by(restaurant_id=restaurant.id).all()
	listMenuItems=[]
	j=0
	for i in menuItems:
		if i.serialize !=[]:
			listMenuItems.append(i.serialize)
		j=j+1
	return jsonify(MenuItems=listMenuItems)

# Making and API endpoint for a single MenuItem(GET Request)
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def menuItemJSON(restaurant_id,menu_id):
	menuItem = session.query(MenuItem).filter_by(id=menu_id,restaurant_id=restaurant_id).one()
	return jsonify(MenuItem=menuItem.serialize)

# Task 1: Create route for Restaurant function here
@app.route('/')
@app.route('/restaurant/')
def restaurantList():
	restaurants = session.query(Restaurant).all()
	#Below code show how to use HTML Template to achieve the same dynamically
	return render_template('restaurant.html',restaurants=restaurants)


# Task 1: Create route for newRestaurant function here
@app.route('/restaurant/new/',methods=['GET','POST'])	
def newRestaurant():
	if 'username' not in login_session:
		return redirect('/login');
	if request.method == 'POST':
		newRestaurant = Restaurant(name=request.form['restaurantname'])
		session.add(newRestaurant)
		session.commit()
		flash('New Restaurant created')
		return	redirect(url_for('restaurantList'))
	else:
		return render_template('newrestaurant.html')
	

# Task 2: Create route for editRestaurant function here
@app.route('/restaurant/<int:restaurant_id>/edit/',methods=['GET','POST'])		
def editRestaurant(restaurant_id):
	if 'username' not in login_session:
		return redirect('/login');	
	editedRestaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	if request.method == 'POST':
		if editedRestaurant !=[]:
			editedRestaurant.name=request.form['restaurantname']
			session.add(editedRestaurant)
			session.commit()
			flash('Restaurant "'+editedRestaurant.name+'" updated successfully')
		return	redirect(url_for('restaurantList',restaurant_id=restaurant_id))

	else:
		return render_template('editrestaurant.html',restaurant_id=restaurant_id,editedRestaurant=editedRestaurant)

# Task 3: Create route for deleteRestaurant function here
@app.route('/restaurant/<int:restaurant_id>/delete/',methods=['GET','POST'])		
def deleteRestaurant(restaurant_id):	
	if 'username' not in login_session:
		return redirect('/login');	
	deletedRestaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	if request.method == 'POST':		
		if deletedRestaurant !=[]:
			session.delete(deletedRestaurant)
			session.commit()
			flash('Restaurant "'+deletedRestaurant.name+'" deleted successfully')
		return	redirect(url_for('restaurantList',restaurant_id=restaurant_id))

	else:
		return render_template('deleterestaurant.html',restaurant_id=restaurant_id,deletedRestaurant=deletedRestaurant)

# Task 5: Create route for newMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def restaurantMenu(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	menuItems = session.query(MenuItem).filter_by(restaurant_id=restaurant.id).all()
	#Below code show how to use HTML Template to achieve the same dynamically
	return render_template('menu.html',restaurant=restaurant,menuItems=menuItems)
	

# Task 6: Create route for newMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/menu/new/',methods=['GET','POST'])	
def newMenuItem(restaurant_id):
	if 'username' not in login_session:
		return redirect('/login');	
	if request.method == 'POST':
		newMenu = MenuItem(name=request.form['newmenu'],price=request.form['price'],description=request.form['description'],restaurant_id=restaurant_id)
		session.add(newMenu)
		session.commit()
		flash('New menu item created')
		return	redirect(url_for('restaurantMenu',restaurant_id=restaurant_id))
	else:
		return render_template('newmenuitem.html',restaurant_id=restaurant_id)
	

# Task 7: Create route for editMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit/',methods=['GET','POST'])		
def editMenuItem(restaurant_id,menu_id):
	if 'username' not in login_session:
		return redirect('/login');	
	editedMenu = session.query(MenuItem).filter_by(id=menu_id).one()
	if request.method == 'POST':
		if editedMenu !=[]:
			editedMenu.name=request.form['editmenu']
			session.add(editedMenu)
			session.commit()
			flash('MenuItem "'+editedMenu.name+'" updated successfully')
		return	redirect(url_for('restaurantMenu',restaurant_id=restaurant_id))

	else:
		return render_template('editmenuitem.html',restaurant_id=restaurant_id,menu_id=menu_id,placeHolderMenu=editedMenu)

# Task 8: Create route for deleteMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete/',methods=['GET','POST'])		
def deleteMenuItem(restaurant_id,menu_id):	
	if 'username' not in login_session:
		return redirect('/login');	
	deletedMenu = session.query(MenuItem).filter_by(id=menu_id).one()
	if request.method == 'POST':		
		if deletedMenu !=[]:
			session.delete(deletedMenu)
			session.commit()
			flash('Menu "'+deletedMenu.name+'" deleted successfully')
		return	redirect(url_for('restaurantMenu',restaurant_id=restaurant_id))

	else:
		return render_template('deletemenuitem.html',restaurant_id=restaurant_id,menu_id=menu_id,deleteItemMenu=deletedMenu)


if __name__ == '__main__':
	app.secret_key = 'Super-Secret-Key'
	app.debug=True
	app.run(host='0.0.0.0',port=8000)
