import os
import sys
import json
import random
import string
import re
from datetime import date
# from app import app
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

# import app.utilities
# from flask import Assets
# from flask.ext.assets import Bundle, Environment

app = Flask(__name__)

app.config.from_pyfile("config.py")
app.secret_key = 'Ev4gloAsQynGg0Puo3nlmY_r'
import routes


# CSRF Protection
# @app.before_request
# def csrf_protect():
#     '''
#             Check csrf_token for every coming post request.
#     '''
#     if (request.method == "POST") or (request.method == "PUT"):
#         token = request.form.get('_csrf_token')
#         if token is None:
#             token = request.args.get('_csrf_token')
#         stored_token = login_session.pop('_csrf_token', None)
#         if not stored_token or stored_token != token:
#             abort(403)
#
#
# def generate_csrf_token():
#     '''
#             Generate a random string as csrf_token
#     '''
#     if '_csrf_token' not in login_session:
#         login_session['_csrf_token'] = utilities.random_state
#     return login_session['_csrf_token']
#
# app.jinja_env.globals['csrf_token'] = generate_csrf_token
