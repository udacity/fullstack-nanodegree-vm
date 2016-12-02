from flask import Flask, render_template, request, redirect, jsonify, \
    url_for, \
    flash, g
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem, User
from flask import session as login_session
from flask.ext.github import GitHub

app = Flask(__name__)
APPLICATION_NAME = "Restaurant Menu Application"
# Connect to Database and create database session
engine = create_engine('sqlite:///restaurantmenuwithusers.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
db_session = DBSession()
# Set these values
GITHUB_CLIENT_ID = 'XXXXXXXXXXXX'
GITHUB_CLIENT_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXX'
app.config.from_object(__name__)
# setup github-flask
github = GitHub(app)


@app.before_request
def before_request():
    g.user = None
    if 'user_id' in login_session:
        g.user = getUserInfo(login_session['user_id'])



@github.access_token_getter
def token_getter():
    return login_session['github_access_token']


@app.route('/github-callback')
@github.authorized_handler
def authorized(access_token):
    next_url = url_for('showRestaurants')
    if access_token is None:
        return redirect(next_url)
    login_session['github_access_token'] = access_token
    # print "hahah:" + str(github.get("user"))
    email = github.get("user").get("email")
    user = getUserByEmail(email)
    if user is None:
        login_session['username'] = github.get("user").get("name")
        login_session['email'] = email
        login_session['picture'] = github.get("user").get("avatar_url")
        login_session['github_access_token'] = access_token
        user = createUser(login_session)
    g.user = user
    login_session['user_id'] = user.id
    login_session['username'] = user.name
    login_session['email'] = user.email
    login_session['picture'] = user.picture
    login_session['github_access_token'] = access_token
    return redirect(next_url)


@app.route('/login')
def showLogin():
    if login_session.get('user_id', None) is None:
        return github.authorize()
        # offline to test this restaurant system
        # login_session['username']='David'
        # login_session['user_id'] = 2
        # return redirect(url_for('showRestaurants'))
    else:
        return redirect(url_for('showRestaurants'))


# User Helper Functions
def createUser(login_session):
    newUser = User(name=login_session['username'],
                   email=login_session['email'],
                   picture=login_session['picture'],
                   github_access_token=login_session['github_access_token'])
    db_session.add(newUser)
    db_session.commit()
    user = db_session.query(User).filter_by(
        github_access_token=login_session['github_access_token']).one()
    return user


def getUserInfo(user_id):
    try:
        user = db_session.query(User).filter_by(id=user_id).one()
        return user
    except:
        return None


def getUserByEmail(email):
    try:
        user = db_session.query(User).filter_by(email=email).one()
        return user
    except:
        return None


# JSON APIs to view Restaurant Information
@app.route('/restaurant/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    restaurant = db_session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = db_session.query(MenuItem).filter_by(
        restaurant_id=restaurant_id).all()
    return jsonify(MenuItems=[i.serialize for i in items])


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def menuItemJSON(restaurant_id, menu_id):
    Menu_Item = db_session.query(MenuItem).filter_by(id=menu_id).one()
    return jsonify(Menu_Item=Menu_Item.serialize)


@app.route('/restaurant/JSON')
def restaurantsJSON():
    restaurants = db_session.query(Restaurant).all()
    return jsonify(restaurants=[r.serialize for r in restaurants])


# Show all restaurants
@app.route('/')
@app.route('/restaurant/')
def showRestaurants():
    restaurants = db_session.query(Restaurant).order_by(asc(Restaurant.name))
    if 'username' not in login_session:
        return render_template('publicrestaurants.html',
                               restaurants=restaurants)
    else:
        return render_template('restaurants.html', restaurants=restaurants,
                               username=login_session['username'])


# Create a new restaurant
@app.route('/restaurant/new/', methods=['GET', 'POST'])
def newRestaurant():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newRestaurant = Restaurant(
            name=request.form['name'], user_id=login_session['user_id'])
        db_session.add(newRestaurant)
        flash('New Restaurant %s Successfully Created' % newRestaurant.name)
        db_session.commit()
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('newRestaurant.html',
                               username=login_session['username'])


# Edit a restaurant


@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    editedRestaurant = db_session.query(
        Restaurant).filter_by(id=restaurant_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if editedRestaurant.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not authorized " \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "to edit this restaurant. Please create your own restaurant " \
               "in order to edit.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        if request.form['name']:
            editedRestaurant.name = request.form['name']
            flash('Restaurant Successfully Edited %s' % editedRestaurant.name)
            return redirect(url_for('showRestaurants'))
    else:
        return render_template('editRestaurant.html',
                               restaurant=editedRestaurant,
                               username=login_session['username'])


# Delete a restaurant
@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    restaurantToDelete = db_session.query(
        Restaurant).filter_by(id=restaurant_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if restaurantToDelete.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not authorized " \
               "" \
               "" \
               "to delete this restaurant. Please create your own restaurant " \
               "" \
               "" \
               "in order to delete.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        db_session.delete(restaurantToDelete)
        flash('%s Successfully Deleted' % restaurantToDelete.name)
        db_session.commit()
        return redirect(
            url_for('showRestaurants', restaurant_id=restaurant_id))
    else:
        return render_template('deleteRestaurant.html',
                               restaurant=restaurantToDelete,
                               username=login_session['username'])


# Show a restaurant menu


@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def showMenu(restaurant_id):
    restaurant = db_session.query(Restaurant).filter_by(id=restaurant_id).one()
    creator = getUserInfo(restaurant.user_id)
    items = db_session.query(MenuItem).filter_by(
        restaurant_id=restaurant_id).all()
    if 'username' not in login_session or creator.id != login_session[
        'user_id']:
        return render_template('publicmenu.html', items=items,
                               restaurant=restaurant, creator=creator)
    else:
        return render_template('menu.html', items=items, restaurant=restaurant,
                               creator=creator,
                               username=login_session['username'])


# Create a new menu item
@app.route('/restaurant/<int:restaurant_id>/menu/new/',
           methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    if 'username' not in login_session:
        return redirect('/login')
    restaurant = db_session.query(Restaurant).filter_by(id=restaurant_id).one()
    if login_session['user_id'] != restaurant.user_id:
        return "<script>function myFunction() {alert('You are not authorized " \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "to add menu items to this restaurant. Please create your own " \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "restaurant in order to add items.');}</script><body " \
               "onload='myFunction()''>"
    if request.method == 'POST':
        newItem = MenuItem(name=request.form['name'],
                           description=request.form['description'],
                           price=request.form[
                               'price'], course=request.form['course'],
                           restaurant_id=restaurant_id,
                           user_id=restaurant.user_id)
        db_session.add(newItem)
        db_session.commit()
        flash('New Menu %s Item Successfully Created' % (newItem.name))
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id,
                               username=login_session['username'])


# Edit a menu item


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit',
           methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedItem = db_session.query(MenuItem).filter_by(id=menu_id).one()
    restaurant = db_session.query(Restaurant).filter_by(id=restaurant_id).one()
    if login_session['user_id'] != restaurant.user_id:
        return "<script>function myFunction() {alert('You are not authorized " \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "to edit menu items to this restaurant. Please create your " \
               "own restaurant in order to edit items.');}</script><body " \
               "onload='myFunction()''>"
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['price']:
            editedItem.price = request.form['price']
        if request.form['course']:
            editedItem.course = request.form['course']
        db_session.add(editedItem)
        db_session.commit()
        flash('Menu Item Successfully Edited')
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('editmenuitem.html',
                               restaurant_id=restaurant_id, menu_id=menu_id,
                               item=editedItem)


# Delete a menu item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete',
           methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    if 'username' not in login_session:
        return redirect('/login')
    restaurant = db_session.query(Restaurant).filter_by(id=restaurant_id).one()
    itemToDelete = db_session.query(MenuItem).filter_by(id=menu_id).one()
    if login_session['user_id'] != restaurant.user_id:
        return "<script>function myFunction() {alert('You are not authorized " \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "" \
               "to delete menu items to this restaurant. Please create your " \
               "own restaurant in order to delete items.');}</script><body " \
               "onload='myFunction()''>"
    if request.method == 'POST':
        db_session.delete(itemToDelete)
        db_session.commit()
        flash('Menu Item Successfully Deleted')
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('deleteMenuItem.html', item=itemToDelete)


# Disconnect based on provider
@app.route('/disconnect')
def disconnect():
    del login_session['username']
    # del login_session['email']
    # del login_session['picture']
    del login_session['user_id']
    flash("You have successfully been logged out.")
    return redirect(url_for('showRestaurants'))


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
