from flask import Flask, render_template, request, redirect, jsonify, url_for, flash


from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User

from flask import session as login_session
import random
import string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

# Load JSON secrets as needed
CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']

APPLICATION_NAME = "Item Catalog"


# Connect to Database and create database session
engine = create_engine('sqlite:///catalogappwithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Front page
@app.route('/')
def showMainPage():
    categories = session.query(Category).order_by(asc(Category.name))
    return render_template('front.html', categories = categories)

# Catalog category management
@app.route('/catalog/<string:category_name>/')
def showCategory(category_name):
    categories = session.query(Category).order_by(asc(Category.name))
    
    category = session.query(Category).filter_by(name=category_name).one()
    
    items = session.query(Item).filter_by(catalog_id=category.id).all()
    
    return render_template('category.html', category=category, items=items)

@app.route('/catalog/new/', methods=['GET', 'POST'])
def newCategory():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newCategory = Category(name=request.form['name'], user_id=login_session['user_id'])
        session.add(newCategory)
        flash('New Category %s Successfully Created' % newCategory.name)
        session.commit()
        return redirect(url_for('showMainPage'))
    else:
        return render_template('newCategory.html')

@app.route('/catalog/<string:category_name>/edit/', methods=['GET', 'POST'])
def editCategory(category_name):
    if 'username' not in login_session:
        return redirect('/login')
    editedCategory = session.query(Category).filter_by(name=category_name).one()
    if editedCategory.user_id != login_session['user_id']:
        return "<script>function badUserAlert() { alert('You are not authorized to edit this category. Please create your own category and you will be able to edit it'); }</script><body onload='badUserAlert()'>"
    if request.method == 'POST':
        if request.form['name']:
            editedCategory.name = request.form['name']
            flash('Category Successfully Edited %s' % editedCategory.name)
            return redirect(url_for('showCategory', category_name=editedCategory.name))
    else:
        return render_template('editCategory.html', category=editedCategory)

@app.route('/catalog/<string:category_name>/delete/', methods=['GET', 'POST'])
def deleteCategory(category_name):
    if 'username' not in login_session:
        return redirect('/login')
    categoryToDelete = session.query(Category).filter_by(name=category_name).one()
    if categoryToDelete.user_id != login_session['user_id']:
        return "<script>function badUserAlert() { alert('You are not authorized to delete this category. Please create your own category and you will be able to delete it'); }</script><body onload='badUserAlert()'>"
    if request.method == 'POST':
        session.delete(categoryToDelete)
        flash('%s Successfully Deleted' % categoryToDelete.name)
        session.commit()
        return redirect(url_for('showMainPage'))
    else:
        return render_template('deleteCategory.html', category=categoryToDelete)

# Catalog item addition
@app.route('/catalog/<string:category_name>/new', methods=['GET', 'POST'])
def newItem(category_name):
    if 'username' not in login_session:
        return redirect('/login')
    category = session.query(Category).filter_by(name=category_name).one()
    if request.method == 'POST':
        newItem = Item(name=request.form['name'], description=request.form['description'], catalog_id=category.id, user_id=login_session['user_id'])
        session.add(newItem)
        session.commit()
        flash('New %s Item Successfully Created' % (newItem.name))
        return redirect(url_for('showCategory', category_name=category_name))
    else:
        return render_template('newItem.html', category_name=category_name)

# Show item information
@app.route('/catalog/<string:category_name>/<string:item_name>')
def showItem(category_name, item_name):
    item = session.query(Item).filter_by(name = item_name).one()
    return render_template('item.html', item=item, category_name=category_name)

# Edit item
@app.route('/catalog/<string:category_name>/<string:item_name>/edit', methods=['GET', 'POST'])
def editItem(category_name, item_name):
    if 'username' not in login_session:
        return redirect('/login')
    editedItem = session.query(Item).filter_by(name=item_name).one()
    if editedItem.user_id != login_session['user_id']:
        return "<script>function badUserAlert() { alert('You are not authorized to edit this item. Please create your own item and you will be able to edit it'); }</script><body onload='badUserAlert()'>"
    categories = session.query(Category).order_by(asc(Category.name))
    category = session.query(Category).filter_by(name=category_name).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        session.add(editedItem)
        session.commit()
        flash('Item Successfully Edited')
        return redirect(url_for('showCategory', category_name=category_name))
    else:
        return render_template('editItem.html', category_name=category_name, item_name=editedItem.name, item=editedItem, categories=categories)


# Delete a menu item
@app.route('/catalog/<string:category_name>/<string:item_name>/delete', methods=['GET', 'POST'])
def deleteItem(category_name, item_name):
    if 'username' not in login_session:
        return redirect('/login')
    category = session.query(Category).filter_by(name=category_name).one()
    itemToDelete = session.query(Item).filter_by(name=item_name).one()
    if itemToDelete.user_id != login_session['user_id']:
        return "<script>function badUserAlert() { alert('You are not authorized to delete this item. Please create your own item and you will be able to delete it'); }</script><body onload='badUserAlert()'>"
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash('Item Successfully Deleted')
        return redirect(url_for('showCategory', category_name=category_name))
    else:
        return render_template('deleteItem.html', item=itemToDelete, category_name=category_name)


# JSON APIs to view items in a Category

# Overview of all items in a category in JSON
@app.route('/catalog/<string:category_name>/JSON')
def catalogItemsJSON(category_name):
    category = session.query(Category).filter_by(name=category_name).one()
    items = session.query(Item).filter_by(catalog_id=category.id).all()
    return jsonify(Items=[i.serialize for i in items])

# Overiew of all items information in JSON
@app.route('/catalog/<string:category_name>/<string:item_name>/JSON')
def itemJSON(category_name, item_name):
    item = session.query(Item).filter_by(name=item_name).one()
    return jsonify(item=item.serialize)

# Overview of all items in catalog in JSON
@app.route('/catalog/JSON')
def catalogJSON():
    categories = session.query(Category).all()
    return jsonify(categories=[c.serialize for c in categories])

# USER LOGIN SYSTEM

# Create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


# attempt google login
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
        response = make_response(json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % access_token)
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
        response = make_response(json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response
        
    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['credentials'] = credentials.access_token
    login_session['gplus_id'] = gplus_id
    
    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)
    
    data = answer.json()
    
    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    
    # See if a user exists, if it doesn't make a new one
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
        login_session['user_id'] = user_id
    
    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output

# User Helper Functions


def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session['email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


# GOOGLE DISCONNECT - Revoke a current user's token and reset their login_session
@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    credentials = login_session.get('credentials')
    if credentials is None:
        response = make_response(json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    
    access_token = login_session.get('credentials')
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['credentials']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]

    if result.status == 200:
        # Reset the user's sesson.
        del login_session['credentials']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        # For whatever reason, the given token was invalid.
        response = make_response(json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response

# Network setup

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
