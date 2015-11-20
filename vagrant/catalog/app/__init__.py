from datetime import datetime
from os import path
from wtforms import Form, BooleanField, StringField, validators
from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask import session, flash, abort, g


app = Flask(__name__)
app.config.from_pyfile('config.cfg')


from app import forms, models, views  # noqa
