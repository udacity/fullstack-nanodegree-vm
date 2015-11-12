import os
import sys
import json
import random
import string
import re
from datetime import date
from app import app
from flask import send_from_directory
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash

# Loading login session library
from flask import session as login_session

import httplib2
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError

from urlparse import urljoin

# For the purpose of providing atome feeds.
from werkzeug.contrib.atom import AtomFeed

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker

import app.utilities as utilities

# Importing Base, CategoryModel, ImageModel, UserModel and ItemsModel.
from models import Base, CategoryModel, ImageModel, UserModel, ItemsModel


# Connect to Database and create database session
# engine = create_engine('postgresql:////localhost//udacity_catalog_db')
engine = create_engine('sqlite:///udacity_catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
# from database_setup import Users, Catalogs, CatalogItems
# from flask.ext.assets import Bundle, Environment


def make_external(url):
    return urljoin(request.url_root, url)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'img/icons/favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/login', methods=['GET', 'POST'])
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return "Current state: %s" % login_session['state']


@app.route("/gconnect/", methods=['POST'])
def gconnect():
    '''
            Api for login using Goople Authentications.
    '''
    print "**********************************"
    print request
    print "**********************************"
    print request.data
    print "**********************************"
    print json.loads(request.data)
    requested_data = request.data

    # Obtaining information about client given access_token
    try:
        oauth_flow = flow_from_clientsecrets(
            app.config['GOOGLE_AUTH'], scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(requested_data)
    except FlowExchangeError:
        return utils.json_response('Failed to upgrade the authorization code', 401)

    access_token = credentials.access_token

    # Avoid duplicated login
    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        return utils.json_response('Current user is already connected', 200)

    login_session['access_token'] = access_token

    # Retrive user info for user
    userinfo_url = 'https://www.googleapis.com/oauth2/v2/userinfo'
    answer = requests.get(userinfo_url, headers={
                          'Authorization': 'Bearer ' + access_token})

    data = json.loads(answer.text)
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    login_session['name'] = data['name']
    login_session['type'] = 'google'

    # Check if the user exist
    user = getUserByEmail(login_session['email'])
    if user is None:
        user = UserModel.add(fullname=login_session['name'], email=login_session[
                             'email'], picture=login_session['picture'])
        session.commit()

    login_session['uuid'] = user.id

    message = {'picture': login_session['picture'], 'email': login_session[
        'email'], 'fullname': login_session['name']}
    return utilities.status(message, 200, 'json')


@app.route("/logout")
def logout():
    if (login_session['type'] == 'google'):
        gdisconnect()
    else:
        return utilities.status(app.config['ERROR_401'], 401)


def gdisconnect():
    '''
            Google oauth server side logout api
    '''
    access_token = login_session.get('access_token')
    if access_token is None:
        return utils.json_response("Current user not connected", 401)
    result = requests.get(
        'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token)
    if result.status_code == requests.codes.ok:
        del login_session['access_token']
        del login_session['email']
    del login_session['name']
    del login_session['picture']
    del login_session['uuid']
    return utilities.status('Successfully disconnected', 200)


@app.route('/category/', methods=['GET'])
@app.route('/category/<format_id>', methods=['GET'])
def categoryModel(format_id=None):
    categories = session.query(CategoryModel).all()

    if format_id is None:
        format_id = ' '

    if (re.compile('\s|\Ajson\Z', re.I).match(format_id) is not None):
        return jsonify(categories=[r.serialize for r in categories])
    elif (re.compile('\Arss\Z', re.I).match(format_id) is not None):
        feed = AtomFeed('Recent Categories',
                        feed_url=request.url, url=request.url_root)
        for category in categories:
            feed.add(category.name, id=category.id, content_type='html',
                     updated=category.created_at,
                     published=category.created_at)

        return feed.get_response()


@app.route('/image/', methods=['GET'])
@app.route('/image/<format_id>/', methods=['GET'])
@app.route('/image/<format_id>/id=<id>', methods=['GET'])
@app.route('/image/<format_id>/category=<catalog_id>', methods=['GET'])
@app.route('/image/<format_id>/id=<id>/category=<catalog_id>', methods=['GET'])
def imageModel(format_id=None, id=None, catalog_id=None):
    try:
        if (catalog_id is None):
            if (id is None):
                images = session.query(ImageModel).all()
            else:
                images = session.query(ImageModel).filter_by(id=id).all()
        else:
            if (id is None):
                images = session.query(ImageModel).filter_by(
                    category_id=catalog_id).all()
            else:
                images = session.query(ImageModel).filter_by(
                    id=id, category_id=catalog_id).all()
    except ValueError:
        print 'ValueError'
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

    if format_id is None:
        format_id = ' '

    if (re.compile('\s|\Ajson\Z', re.I).match(format_id) is not None):
        return jsonify(images=[r.serialize for r in images])
    elif (re.compile('\Arss\Z', re.I).match(format_id) is not None):
        try:
            feed = AtomFeed('Recent list of images available.',
                            feed_url=request.url, url=request.url_root)
            for image in images:
                feed.add(image.id, image.path,
                         id=image.id,
                         content_type='html',
                         updated=image.created_at,
                         published=image.created_at)

            return feed.get_response()
        except:
            print "Unexpected error:", sys.exc_info()
            print "Unexpected error:", sys.exc_info()[0]
            raise


@app.route('/items/', methods=['GET'])
@app.route('/items/<format_id>/', methods=['GET'])
@app.route('/items/<format_id>/category=<catalog_id>', methods=['GET'])
def itemsModel(format_id=None, catalog_id=None):
    try:
        if (catalog_id is None):
            items = session.query(ItemsModel).all()
        else:
            items = session.query(ItemsModel).filter_by(
                category_id=catalog_id).all()
    except ValueError:
        print 'ValueError'
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

    if format_id is None:
        format_id = ' '

    if (re.compile('\s|\Ajson\Z', re.I).match(format_id) is not None):
        return jsonify(items=[r.serialize for r in items])


@app.route('/item/delete/<item_id>', methods=['POST'])
def deleteItem(item_id):
    print item_id
    itemToDelete = session.query(ItemsModel).filter_by(id=item_id).one()
    print itemToDelete
    session.delete(itemToDelete)
    session.commit()
    return render_template('index.html')


@app.route('/item/edit/<item_id>/', methods=['PUT'])
def editItem(item_id):
    item = session.query(ItemsModel).filter_by(id=item_id).one()

    # Loading data from request
    data = json.loads(request.data)
    item.category_id = data["category_id"]
    item.title = data["title"]
    item.description = data["description"]
    item.image_id = data["image_id"]

    # Saving information
    session.add(item)
    session.commit()
    return render_template('index.html')

    @app.route('/item/new/', methods=['POST'])
    def addItem():
        # Loading data from request
        data = json.loads(request.data)

        # Inserting new data
        item_model = ItemsModel(
            id=re.sub(r"[+=\/]", "_", base64.b64encode(uuid.uuid4().bytes)),
            category_id=data["category_id"],
            title=data["title"],
            description=data["description"],
            image_id=data["image_id"],
            user_id=getCurrentUser().id)

        # Saving information
        session.add(item)
        session.commit()
        return render_template('index.html')

    def getUserById(id):
        try:
            return session.query(UserModel).filter_by(id=id).one()
        except:
            return None

        def getUserByEmail(email):
            try:
                user = session.query(UserModel).filter_by(email=email).one()
                return user.id
            except:
                return None
