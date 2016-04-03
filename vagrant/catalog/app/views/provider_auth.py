'''
This page module simply loads the data for the app as json endpoints.
	The module contents only respond to get requests.
'''
import os
import sys
import json
import random
import string
import re
import requests
import urllib
import traceback
from functools import wraps
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError

from flask import Flask, Blueprint, g, current_app, Response, request, abort, render_template, make_response, flash, redirect, url_for
from werkzeug import secure_filename
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from functools import wraps

# Loading login session library
from flask import session as login_session

import app as app

from app import utilities

import app.models as models
from app.models import data_models as data_models
from app.models.data_models import Base, CategoryModel, ImageModel, UserModel, ItemsModel

engine = create_engine('postgresql://catalog:passDB@localhost/CatalogDb')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

module = Blueprint('provider_auth', __name__)


@module.route("/glogin", methods=['POST'])
def gconnect():
    '''
            Api for login using Goople Authentications.
    '''
    # loading code
    code = request.data
    try:
        oauth_flow = flow_from_clientsecrets(
            'client_secret.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        print "Unexpected error:", sys.exc_info()[0]
        print "Unexpected error:", sys.exc_info()[1]
        return utilities.status('Failed to upgrade the authorization code', 401, 'json')
    except:
        print "Unexpected error:", sys.exc_info()[0]
        print "Unexpected error:", sys.exc_info()[1]
        abort(404)

    access_token = credentials.access_token
    provider_id = credentials.id_token['sub']

    # Avoid duplicated login
    stored_access_token = login_session.get('access_token')
    stored_provider_id = login_session.get('provider_id')

    if stored_access_token is not None and provider_id == stored_provider_id:
        return utilities.status(login_session.get('message'), 200, 'json')

    # Storing access token
    login_session['access_token'] = access_token

    # Retrive user info for user
    userinfo_url = 'https://www.googleapis.com/oauth2/v2/userinfo'
    answer = requests.get(userinfo_url, headers={
                          'Authorization': 'Bearer ' + access_token})

    data = json.loads(answer.text)
    # Check if the user exist
    user = models.select_user_by_email(data['email'])

    if user is None:
        user = models.insert_new_user(data['name'], data[
                                      'email'], data['picture'].strip('/'))
    login_session['provider_id'] = provider_id
    login_session['email'] = data['email']
    login_session['message'] = {'picture': data['picture'].strip('/'), 'email': data[
        'email'], 'fullname': data['name'], 'id': user.id, 'provider': 'google'}

    return utilities.status(login_session.get('message'), 200, 'json')


@module.route("/glogout", methods=['POST'])
@utilities.require_login
def gdisconnect():
    '''
            Google oauth server side logout api
    '''
    access_token = login_session.get('access_token')
    if access_token is None:
        return utilities.status("Current user not connected", 401, 'json')
    result = requests.get(
        'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token)

    return disconnect(result.status_code)


@module.route("/flogin", methods=['POST'])
def fconnect():
    '''
            Api for login using Facebook Authentications.
    '''
    # loading code
    data = json.loads(request.data)
    access_token = data['authResponse']['accessToken']
    provider_id = data['id']

    # Avoid duplicated login
    stored_access_token = login_session.get('access_token')
    stored_provider_id = login_session.get('provider_id')

    if stored_access_token is not None and provider_id == stored_provider_id:
        return utilities.status(login_session.get('message'), 200, 'json')

    # Storing access token
    login_session['access_token'] = access_token
    # Check if the user exist
    user = models.select_user_by_email(data['email'])
    if user is None:
        user = models.insert_new_user(data['name'], data[
                                      'email'], data['picture']['data']['url'].strip('/'))

    login_session['provider_id'] = provider_id
    login_session['email'] = data['email']
    login_session['message'] = {'picture': data['picture']['data']['url'].strip('/'), 'email': data[
        'email'], 'fullname': data['name'], 'id': user.id, 'provider': 'facebook'}

    return utilities.status(login_session.get('message'), 200, 'json')


@module.route("/flogout", methods=['POST'])
@utilities.require_login
def fdisconnect():
    '''
            Facebook oauth server side logout api
    '''
    access_token = login_session.get('access_token')

    if access_token is None:
        return utilities.status("Current user not connected", 401, 'json')
    return disconnect(requests.codes.ok)


@utilities.require_login
def disconnect(result):
    '''
            Single method remove all related information to disconnect.
    '''
    if result == requests.codes.ok:
        del login_session['access_token']
        del login_session['email']
        del login_session['message']
        del login_session['provider_id']

    return utilities.status('Successfully disconnected', 200, 'json')
