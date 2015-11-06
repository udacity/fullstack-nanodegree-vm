from datetime import datetime
from os import path
from wtforms import Form, BooleanField, StringField, validators
from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask import session, flash, abort, g
from flask.ext.sqlalchemy import SQLAlchemy, Pagination
from sqlalchemy.sql import func, desc
from flask.ext.login import LoginManager, login_user
from flask.ext.login import logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
import flask.ext.whooshalchemy as whooshalchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'

from app import forms, models, views  # noqa
