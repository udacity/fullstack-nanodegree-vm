'''
    The api is designed to commit to update or delete an item.
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

module = Blueprint('update_api', __name__)


@module.route('/item/delete/<item_id>', methods=['POST'])
@utilities.require_login
def deleteItem(item_id):
    itemToDelete = models.select_item_by_id(item_id)
    models.delete_item(itemToDelete)
    return utilities.status('Successfully deleted', 200, 'json')


@module.route('/item/edit/<item_id>/', methods=['PUT'])
@utilities.require_login
def editItem(item_id):
    item = models.select_item_by_id(item_id)

    # Loading data from request
    data = json.loads(request.data)
    models.update_item(item, data["title"], data["description"], data[
                       "image_id"], data["category_id"])
    return utilities.status('Successfully updated', 200, 'json')


@module.route('/item/new', methods=['POST'])
@utilities.require_login
def addItem():
    # Loadind user information
    user_id = models.select_user_by_email(login_session.get('email')).id
    # Loading data from request
    data = json.loads(request.data)
    models.insert_new_item(user_id, data["title"], data["description"], data[
                           "category_id"], data["image_id"])
    return utilities.status('Successfully inserted', 200, 'json')
