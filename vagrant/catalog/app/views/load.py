'''
This page module simply loads the data for the app
'''
from flask import Blueprint, render_template, session, redirect, url_for, \
     request, flash, g, jsonify, abort

# Loading login session library
from flask import session as login_session

from app import utilities

module = Blueprint('page', __name__)

@module.route('/')
@module.route('/index')
def index():
    return render_template('index.html')
