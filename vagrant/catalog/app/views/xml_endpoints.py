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

from app import utilities
# from app import utilities.status as status
# from app import utilities.convert_object_to_xml as convert_object_to_xml
# from app import utilities.convert_list_to_xml as convert_list_to_xml


from flask import Blueprint, render_template, redirect, url_for, \
    request, flash, g, jsonify, abort

# Loading login session library
from flask import session as login_session

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker

from app import utilities

import app.models as models
from app.models import data_models as data_models
from app.models.data_models import Base, CategoryModel, ImageModel, UserModel, ItemsModel

engine = create_engine('sqlite:///udacity_catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

module = Blueprint('xml_endpoints', __name__)


@module.route('/category/xml', methods=['GET'])
def categoryModel():
    try:
        categories = models.load_categories()
        if categories is None:
            abort(403)
        else:
            return utilities.status(utilities.convert_list_to_xml('catalogs',
                                                                  [utilities.convert_object_to_xml('catalog',
                                                                                                   r.serialize) for r in categories]), 200, 'xml')
    except:
        print "Unexpected error:", sys.exc_info()[0]
        print "Unexpected error:", sys.exc_info()[1]
        abort(403)


@module.route('/image/xml/id=<id>', methods=['GET'])
def imageModel(id):
    try:
        image = models.select_image_by_id(id)
        if image is None:
            abort(403)
        else:
            print image.serialize
            return utilities.status(utilities.convert_object_to_xml('image', image.serialize), 200, 'xml')
    except:
        print "Unexpected error:", sys.exc_info()[0]
        print "Unexpected error:", sys.exc_info()[1]
        abort(403)


@module.route('/images/xml', methods=['GET'])
@module.route('/images/xml/category_id=<category_id>', methods=['GET'])
def imagesModel(category_id=None):
    try:
        images = None
        if (category_id is None):
            images = models.load_all_images()
        else:
            images = models.load_all_images_by_category(category_id)

        if images is None:
            abort(403)
        else:
            return utilities.status(utilities.convert_list_to_xml('images',
                                                                  [utilities.convert_object_to_xml('image',
                                                                                                   r.serialize) for r in images]), 200, 'xml')
    except:
        print "Unexpected error:", sys.exc_info()[0]
        print "Unexpected error:", sys.exc_info()[1]
        abort(403)


@module.route('/items/xml', methods=['GET'])
@module.route('/items/xml/category_id=<category_id>', methods=['GET'])
@module.route('/items/xml/user_id=<user_id>', methods=['GET'])
@module.route('/items/xml/category_id=<category_id>/user_id=<user_id>', methods=['GET'])
def itemModel(category_id=None, user_id=None):
    try:
        items = None
        if (category_id is None and user_id is None):
            items = models.select_all_items()
        elif (category_id is not None and user_id is None):
            items = models.select_items_by_category(category_id)
        elif (category_id is None and user_id is not None):
            items = models.select_items_by_user_id(user_id)
        else:
            items = models.select_items_by_user_id_and_category_id(
                user_id, category_id)

        if items is None:
            abort(403)
        else:
            return utilities.status(utilities.convert_list_to_xml('items',
                                                                  [utilities.convert_object_to_xml('item',
                                                                                                   r.serialize) for r in items]), 200, 'xml')
    except:
        print "Unexpected error:", sys.exc_info()[0]
        print "Unexpected error:", sys.exc_info()[1]
        abort(403)
