from flask import Flask, render_template, url_for, redirect, request, flash, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem, User

from flask import session as login_session
import random, string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Restauranterator"

# Create database
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)

# Create database connector
DBSession = sessionmaker(bind = engine)
session = DBSession()

# Common urls
restaurant_url = '/restaurant/<int:restaurant_id>'
menu_id_url = restaurant_url + '/menu/<int:menu_id>'

# Methods used
methods = ['GET', 'POST']

# Helper functions
def get_restaurant_by_id(restaurant_id):
    """
    Function for getting a restaurant object given the restaurant id.
    """
    return session.query(Restaurant).filter_by(id = restaurant_id).first()

def get_menu_item_by_id(menu_id):
    """
    Function for getting a menu item object given the menu item id.
    """
    return session.query(MenuItem).filter_by(id = menu_id).first()

def create_user(login_session):
    new_user = User(name=login_session['username'],
                    email=login_session['email'],
                    picture=login_session['picture'])
    session.add(new_user)
    session.commit()
    return get_user_id_by_email(login_session['email'])

def get_user_by_id(user_id):
    """Function for getting a user object given the user id."""
    return session.query(User).filter_by(id = user_id).one()

def get_user_id_by_email(email):
    """
    Function for getting the user id for the given email. If the user
    id cannot be found, returns None.
    """
    try:
        user = session.query(User).filter_by(email = email).one()
        return user.id
    except:
        return None

def get_restaurant_menu_items_by_id(restaurant_id):
    """Returns the menu items for the given restaurant id."""
    return session.query(MenuItem).filter_by(
        restaurant_id = restaurant_id).all()

def make_json_response(message, code):
    """
    Returns a json response with the given message and code.

    response = make_json_response("Invalid state", 401)
    """
    response = make_response(json.dumps(message), code)
    response.headers['Content-Type'] = 'application/json'
    return response


@app.route('/gconnect', methods=['POST'])
def gconnect():
    """Logs the user in using Google third party authentication."""

    if request.args.get('state') != login_session['state']:
        return make_json_response('Invalid state parameter', 401)
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        return make_json_response(
            'Failed to upgrade the authorization code', 401)

    # Check that the access token is valid
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % (
        access_token))
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])

    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        return make_json_response(result.get('error'), 500)

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        message = "Token's user ID doesn't match given user ID."
        return make_json_response(message, 401)

    # Verify that the access token is valid for this app
    if result['issued_to'] != CLIENT_ID:
        message = "Token's client ID does not match app's."
        print message
        return make_json_response(message, 401)

    # Check to see if user is already logged in
    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        return make_json_response('Current user is already connected.', 200)

    # Store the access token in the session for later use.
    login_session['credentials'] = credentials
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt' : 'json'}
    answer = requests.get(userinfo_url, params=params)
    data = json.loads(answer.text)

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # See if user exists, and create the user.
    user_id = get_user_id_by_email(login_session['email'])
    if not user_id:
        user_id = create_user(login_session)

    login_session['user_id'] = user_id


    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("You are now logged in as %s" % login_session['username'])
    print "done!"
    return output

@app.route("/gdisconnect")
def gdisconnect():
    """
    Disconnects a logged in user. Should only be used with
    a connected user.
    """
    credentials = login_session.get('credentials')
    if credentials is None:
        return make_json_response("Current user not connected.", 401)

    # Execute HTTP GET request to revoke current token.
    access_token = credentials.access_token
    url = ('https://accounts.google.com/o/oauth2/revoke?token=%s' % (
        access_token))
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]

    if result['status'] == '200':
        # Reset the users session.
        del login_session['credentials']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']

        return make_json_response('Successfully disconnected.', 200)
    else:
        # For whatever reason, the given token was invalid.
        return make_json_response(
            'Failed to revoke token for given user.', 400)

@app.route('/login/')
def show_login():
    state = ''.join(random.choice(
        string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/')
@app.route('/restaurants/')
def all_restaurants():
    restaurants = session.query(Restaurant).all()
    if 'username' not in login_session:
        return render_template(
            'public_restaurants.html', restaurants=restaurants)
    else:
        return render_template(
            'all_restaurants.html', restaurants=restaurants)

@app.route('/restaurants/json/')
@app.route('/restaurants/JSON/')
def all_restaurants_json():
    restaurants = session.query(Restaurant).all()
    return jsonify(Restaurant=[rest.serialize for rest in restaurants])


@app.route('/restaurant/new/', methods=methods)
def new_restaurant():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        restaurant_name = request.form['name']
        if restaurant_name:
            new_rest = Restaurant(
                name=request.form['name'], user_id=login_session['user_id'])
            session.add(new_rest)
            session.commit()
            flash("New restaurant, %s, created!" % new_rest.name)
            return redirect(url_for('all_restaurants'))
        else:
            flash("Please enter a restaurant name!")
            return render_template('new_restaurant.html')

    else:
        return render_template('new_restaurant.html')

@app.route(restaurant_url + '/')
@app.route(restaurant_url + '/menu/')
def restaurant_menu(restaurant_id):
    restaurant = get_restaurant_by_id(restaurant_id)
    items = get_restaurant_menu_items_by_id(restaurant.id)
    creator = get_user_by_id(restaurant.user_id)
    if login_session['user_id']:
        if restaurant.user_id = login_session['user_id']:
            return render_template('menu.html',
                                   restaurant=restaurant,
                                   items=items,
                                   creator=creator)
    else:
        return render_template('public_menu.html',
                               restaurant=restaurant,
                               items=items,
                               creator=creator)

@app.route(restaurant_url + '/menu/json/')
@app.route(restaurant_url + '/menu/JSON/')
def restaurant_menu_json(restaurant_id):
    restaurant = get_restaurant_by_id(restaurant_id)
    items = get_restaurant_menu_items_by_id(restaurant_id)
    return jsonify(MenuItem=[item.serialize for item in items])

@app.route(restaurant_url + '/edit/', methods=methods)
def edit_restaurant(restaurant_id):
    if 'username' not in login_session:
        return redirect('/login')
    restaurant = get_restaurant_by_id(restaurant_id)
    if login_session['user_id']:
        if restaurant.user_id != login_session['user_id']:
            return redirect(url_for('all_restaurants'))
    else:
        if request.method == 'POST':
            restaurant_name = request.form['name']
            if restaurant_name:
                old_name = restaurant.name
                restaurant.name = restaurant_name
                session.add(restaurant)
                session.commit()
                flash('%s is now named %s!' % (old_name, restaurant.name))
                return redirect(url_for(
                    'restaurant_menu', restaurant_id=restaurant.id))
        else:
            flash("Please enter a restaurant name!")
            return render_template('edit_restaurant.html',
                                   restaurant=restaurant,
                                   restaurant_id=restaurant_id)
        if restaurant:
            return render_template('edit_restaurant.html',
                                   restaurant=restaurant,
                                   restaurant_id=restaurant_id)
        else:
            return redirect(url_for('all_restaurants'))

@app.route(restaurant_url + '/delete/', methods=methods)
def delete_restaurant(restaurant_id):
    if 'username' not in login_session:
        return redirect('/login')
    restaurant = get_restaurant_by_id(restaurant_id)
    if login_session['user_id']:
        if restaurant.user_id != login_session['user_id']:
            return redirect(url_for('all_restaurants'))
    else:
        if restaurant:
            if request.method == 'POST':
                if request.form['Delete']:
                    deleted_name = restaurant.name
                    session.delete(restaurant)
                    session.commit()
                    flash('%s was deleted.' % deleted_name)
                    return redirect(url_for('all_restaurants'))
            else:
                return render_template('delete_restaurant.html',
                                       restaurant=restaurant,
                                       restaurant_id=restaurant_id)
        else:
            return redirect(url_for('all_restaurants'))

@app.route(restaurant_url + '/menu/new/', methods=methods)
def new_menu_item(restaurant_id):
    if 'username' not in login_session:
        return redirect('/login')
    restaurant = get_restaurant_by_id(restaurant_id)
    if restaurant:
        if login_session['user_id']:
            if restaurant.user_id != login_session['user_id']:
                return redirect(url_for(
                    'restaurant_menu', restaurant_id=restaurant_id))
            else:
                if request.method == 'POST':
                    new_item_data = {
                        'name' : request.form['name'],
                       'price' : request.form['price'],
                        'description' : request.form['description'],
                        'course' : request.form['course']
                    }
                    missing_items = []
                    for name, data in new_item_data.iteritems():
                        if not new_item_data[name]:
                            missing_items.append(name)
                    if missing_items:
                        flash("Please enter an item %s!" % (missing_items,))
                        return render_template(
                            'new_menu_item.html', restaurant=restaurant,
                            name_val=new_item_data['name'],
                            desc_val=new_item_data['description'],
                            price_val=new_item_data['price'],
                            course_val=new_item_data['course'])
                    else:
                        new_item = MenuItem(
                            name=new_item_data['name'],
                            description=new_item_data['description'],
                            price=int(new_item_data['price']),
                            course=new_item_data['course'],
                            restaurant_id=restaurant.id,
                            user_id=login_session['user_id'])
                        session.add(new_item)
                        session.commit()
                        flash("New menu item, %s, created!" % new_item.name)
                        return redirect(url_for(
                            'restaurant_menu', restaurant_id=restaurant.id))
                else:
                    return render_template('new_menu_item.html',
                                           restaurant=restaurant)
        else:
            return redirect(url_for('all_restaurants'))

@app.route(menu_id_url + '/edit/', methods=methods)
def edit_menu_item(restaurant_id, menu_id):
    if 'username' not in login_session:
        return redirect('/login')
    restaurant = get_restaurant_by_id(restaurant_id)
    edited_item = get_menu_item_by_id(menu_id)
    if not restaurant or not edited_item:
        return redirect(url_for('all_restaurants'))
    else:
        if restaurant.user_id != login_session['user_id']:
            return redirect(url_for(
                'restaurant_menu', restaurant_id=restaurant_id))
        if edited_item.restaurant_id != restaurant.id:
            flash('Sorry, that menu item does not belong to this restaurant.')
            return redirect('restaurant_menu', restaurant_id=restaurant.id)
        else:
            if request.method == 'POST':
                new_item_data = {
                    'name' : request.form['name'],
                    'price' : request.form['price'],
                    'description' : request.form['description'],
                    'course' : request.form['course']
                }
                missing_items = []
                for name, data in new_item_data.iteritems():
                    if not new_item_data[name]:
                        missing_items.append(name)
                if missing_items:
                    flash("Please enter an item %s!" % missing_items)
                    return render_template('edit_menu_item.html',
                                           restaurant=restaurant,
                                           item=edited_item)
                else:
                    edited_item.name = new_item_data['name']
                    edited_item.price = new_item_data['price']
                    edited_item.description = new_item_data['description']
                    edited_item.course = new_item_data['course']
                    session.add(edited_item)
                    session.commit()
                    flash('%s has been updated!' % (edited_item.name))
                    return redirect(url_for(
                        'restaurant_menu', restaurant_id=restaurant.id))
            else:
                return render_template('edit_menu_item.html',
                                       restaurant=restaurant,
                                       item=edited_item)

@app.route(menu_id_url + '/delete/', methods=methods)
def delete_menu_item(restaurant_id, menu_id):
    if 'username' not in login_session:
        return redirect('/login')
    restaurant = get_restaurant_by_id(restaurant_id)
    to_delete_item = get_menu_item_by_id(menu_id)
    if not restaurant or not to_delete_item:
        return redirect(url_for('all_restaurants'))
    else:
        if restaurant.user_id != login_session['user_id']:
            return redirect(url_for(
                'restaurant_menu', restaurant_id=restaurant_id))
        if to_delete_item.restaurant_id != restaurant.id:
            flash('Sorry, that menu item does not belong to this restaurant.')
            return redirect('restaurant_menu', restaurant_id=restaurant.id)
        else:
            if request.method == 'POST':
                if request.form['Delete']:
                    session.delete(to_delete_item)
                    session.commit()
                    flash('%s was deleted.' % to_delete_item.name)
                return redirect(url_for('restaurant_menu',
                                        restaurant_id=restaurant_id))
            else:
                return render_template('delete_menu_item.html',
                                       restaurant=restaurant,
                                       item=to_delete_item)

@app.route(menu_id_url + '/json/')
@app.route(menu_id_url + '/JSON/')
def menu_item_json(restaurant_id, menu_id):
    menu_item = get_menu_item_by_id(menu_id)
    return jsonify(MenuItems=[menu_item.serialize])



if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)