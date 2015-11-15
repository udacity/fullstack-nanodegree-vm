'''
This page module simply loads the app
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


@module.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'img/icons/favicon.ico', mimetype='image/vnd.microsoft.icon')
