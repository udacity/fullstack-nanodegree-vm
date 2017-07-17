import random, string, json, httplib2
from flask import Flask, render_template, request, redirect, jsonify, make_response, flash
from db import Category, Item, User, DBSession
from sqlalchemy import desc
from flask import session as login_session
from oauth2client.client import FlowExchangeError, flow_from_clientsecrets
import requests

app = Flask(__name__, static_url_path="/static")
session = DBSession()

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read()
)['web']['client_id']
APPLICATION_NAME = "Restaurant Menu Application"

def get_all_categories():
    return session.query(Category).order_by(Category.name).all()

def get_recent_items():
    return session.query(Item).order_by(desc(Item.created_at)).all()

def get_category_by_id(id):
    return session.query(Category).filter(Category.id == id).first()

def get_item_by_id(id):
    return session.query(Item).filter(Item.id == id).first()

@app.route('/')
def main():
    return render_template('main.html', categories=get_all_categories(), items=get_recent_items())

@app.route('/catalog.json')
def catalog_json():
    return jsonify({'json will go here': 'yeah' })

# TODO - cateogry and item pages should perhaps takes slugs instead of ids at some point
@app.route('/category/<int:category_id>')
def category(category_id):
    return render_template('category.html', categories=get_all_categories(), category=get_category_by_id(category_id))

@app.route('/item/<int:item_id>')
def item(item_id):
    return render_template('item.html', item=get_item_by_id(item_id))

@app.route('/item/new', methods=['GET', 'POST'])
def create_item():
    if request.method == 'GET':
        return render_template('new-item.html', categories=get_all_categories())
    else:
        name = request.form['name']
        description = request.form['description']
        category_id = request.form['category']

        new_item = Item(name=name, description=description, category_id=category_id)
        session.add(new_item)
        session.commit()

        return redirect('/', code=303)

@app.route('/item/edit/<int:item_id>', methods=['GET', 'PUT'])
def edit_item(item_id):
    if request.method == 'GET':
        return render_template('edit-item.html', categories=get_all_categories(), item=get_item_by_id(item_id))
    else:
        name = request.form['name']
        description = request.form['description']
        category_id = request.form['category']

        # @TOOD - return errors if name or category is empty
        item = get_item_by_id(item_id)
        item.name = name
        item.category_id = category_id
        item.description = description
        session.add(item)
        session.commit()

        return redirect('/', code=303)

@app.route('/item/delete/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = get_item_by_id(item_id)
    session.delete(item)
    session.commit()
    
    return redirect('/', code=303)


# Create anti-forgery state token
# Create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


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

    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['credentials'] = credentials
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
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output

@app.route('/gdisconnect')
def gdisconnect():
    print login_session
    access_token = login_session.get('access_token')
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: ' 
    print login_session['username']
    if access_token is None:
    	response = make_response(json.dumps('Current user not connected.'), 401)
    	response.headers['Content-Type'] = 'application/json'
    	return response
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



if __name__ == '__main__':
    # @TODO change secret key
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    # @TODO - remove debug mode
    app.run(host='0.0.0.0', port=8000, debug=True)

