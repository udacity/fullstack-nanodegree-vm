# from flask import Flask, session, g, render_template, request, redirect, url_for, abort, flash
from flask import Flask, Blueprint, current_app, Response, request, abort, render_template, make_response, flash, redirect, url_for
from werkzeug import secure_filename
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from functools import wraps
import random
import string
import os
import sys
import json
import time
import hashlib
import requests
import urllib
import webapp2
import jinja2
import traceback
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError

# Loading login session library
from flask import session as login_session

app = Flask(__name__)

app.config.from_pyfile("config.py")
from app import utilities

from app import views

from app.views import page
app.register_blueprint(page.module)

from app.views import json_endpoints
app.register_blueprint(json_endpoints.module)

from app.views import xml_endpoints
app.register_blueprint(xml_endpoints.module)

from app.views import rss_endpoints
app.register_blueprint(rss_endpoints.module)

from app.views import provider_auth
app.register_blueprint(provider_auth.module)

from app.views import update_api
app.register_blueprint(update_api.module)

from app import models
from app.models import data_models
from app.models.data_models import Base, CategoryModel, ImageModel, UserModel, ItemsModel
app.register_blueprint(data_models.data)

app.secret_key = utilities.random_state()


# CSRF Protection
@app.before_request
def csrf_protect():
    '''
            Check csrf_token for every coming post request.
    '''
    if (request.method == "POST") or (request.method == "PUT"):
        token = request.cookies.get('X-Csrf-Token')
        poken = request.headers.get('X-Csrf-Token')
        try:
            stored_token = login_session.pop('_csrf_token', None)
            if not stored_token and not (stored_token == token or stored_token == poken):
                abort(403)
        except:
            print "Unexpected error:", sys.exc_info()[0]
            print "Unexpected error:", sys.exc_info()[1]
            abort(403)


@app.after_request
def reset_token(response):
    '''
            Update cookie token.
    '''
    if (request.method == "POST") or (request.method == "PUT"):
        response.set_cookie('X-Csrf-Token', generated_csrf_token())
    return response


def generated_csrf_token():
    '''
            Generate a random string as csrf_token
    '''
    if '_csrf_token' not in login_session:
        login_session['_csrf_token'] = utilities.random_state()
    return login_session['_csrf_token']

app.jinja_env.globals['csrf_token'] = generated_csrf_token
