#!/usr/bin/python

from flask import Flask,render_template, request, redirect, jsonify, \
     url_for, flash, abort
from sqlalchemy import create_engine,asc,desc
from sqlalchemy.orm import sessionmaker
from dbset import Base, User, Category, Item
from flask import session as login_session
from flask import make_response
import string
import random
import httplib2
import json
import requests

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from oauth2client.client import AccessTokenCredentials

engine = create_engine('sqlite:///data.db')
Base.metadata.bind=engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

app = Flask(__name__)
app.secret_key = 'My_secret_key'

CLIENT_ID = json.loads(
    open('clientSecrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "auth (online item catalog)"


@app.route('/login')
def new_state():
    state = ''.join(random.choice(string.ascii_uppercase +
                    string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('google_login.html',STATE=state)


@app.route('/')
@app.route('/home')
def main_page():
    co=session.query(Category).all()
    c1=session.query(Item).all()
    return render_template('main_pages.html' ,cat_name=co,it_nam=c1)


@app.route('/<int:ids>/')
def main_page1(ids):
    if ids<4:
        c1=session.query(Item).filter_by(category_id=ids).all()
        return render_template('sub_pages.html',
                               item_name=c1)
    else:
        abort(404)


# deleting items
@app.route('/<int:ids>/<string:it>/delete')
def del_item(ids,it):
    user_id = login_session.get('user_id')
    if user_id is None:
        return redirect('/login')
    c=session.query(Item).filter_by(name=it).one()
    if c.user_id != login_session['user_id']:
        return abort(401)
    session.delete(c)
    session.commit()
    return redirect(url_for('main_page1',ids=ids))


# adding new items
@app.route('/<int:ids>/addNew')
# sends to a form page where data is entered
def add_item(ids):
     return render_template('new_item.html',ids=ids)


@app.route('/<int:ids>/forms',methods=['GET', 'POST'])
# requests  entered data from the form
def add_item1(ids):
    names=request.form.get('names')
    description=request.form.get('description')
    if names and description:
        itemNew = Item(
                    name=names,
                    description=description,
                    category_id=ids,
                    user_id = login_session['user_id']
                   )
        session.add(itemNew)
        session.commit()
        return redirect(url_for('main_page1',ids=ids))
    else:
        flash('Fill all the fields !!')
        return render_template('new_item.html',ids=ids)


# editing existing cities
@app.route('/<int:ids>/<int:id2>/edit')
def edit_item(ids,id2):
    id1=session.query(Item).filter_by(id=id2).one()
    user_id = login_session.get('user_id')
    if user_id is None:
        return redirect('/login')
    if id1.user_id != login_session['user_id']:
        return abort(401)
    return render_template('editItem.html',ids=ids,id2=id2,
            it_nme=id1.name,it_des=id1.description)


@app.route('/<int:ids>/<int:id2>/form',methods=['GET', 'POST'])
def edit_item1(ids,id2):
    names=request.form.get('names')
    description=request.form.get('description')
    if names and description:
        c3=session.query(Item).filter_by(id=id2).one()
        c3.name=names
        c3.description=description
        c3.category_id=ids
        session.commit()
        return redirect(url_for('main_page1',ids=ids))
    else:
        id1=session.query(Item).filter_by(id=id2).one()
        flash('Fill all the fields !!')
        return render_template('editItem.html',ids=ids,id2=id2,
               it_nme=id1.name,it_des=id1.description)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    """ Logs user in using his google account."""
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'),
                                 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('clientSecrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    print access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'

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
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    # Check whether user is already logged in
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(
            json.dumps('Current user is already connected.'),
            200)
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
    login_session['email'] = data['email']
    login_session['provider'] = 'google'

    # See if user exists, otherwise create new user
    user_id = get_user_id(data["email"])
    if not user_id:
        user_id = create_user(login_session)
    login_session['user_id'] = user_id
    return "Success!"


def create_user(login_session):
    """ Create new user based on information gathered from OAuth
    providers. """
    new_user = User(name=login_session['username'], email=login_session[
        'email'])
    session.add(new_user)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def get_user_info(user_id):
    """ Get information about the user from his id. """
    user = session.query(User).filter_by(id=user_id).one()
    return user


def get_user_id(email):
    """ Get user_id from his email address. """
    try:
        user = session.query(User).filter_by(email=email).one_or_none()
        return user.id
    except:
        return None


@app.route('/gdisconnect')
def gdisconnect():
    """ Logs user out of his google account."""
    # Only disconnect a connected user.
    credentials = login_session.get('credentials')
    if credentials is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % credentials
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] != '200':
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        del login_session['credentials']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['provider']
        del login_session['user_id']
        response = make_response(json.dumps('Successfully disconnected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response


@app.route('/data.json')
def category_json():
    """ JSON APIs to view Catalog Information. """
    category = session.query(category).all()
    return jsonify(Category=[i.serialize for i in categories])

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
