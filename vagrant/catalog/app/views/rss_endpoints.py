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

from flask import Blueprint, render_template, redirect, url_for, \
    request, flash, g, jsonify, abort

# Loading login session library
from flask import session as login_session

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker

# For the purpose of providing atome feeds.
from werkzeug.contrib.atom import AtomFeed

from app import utilities

import app.models as models
from app.models import data_models as data_models
from app.models.data_models import Base, CategoryModel, ImageModel, UserModel, ItemsModel

engine = create_engine('postgresql://catalog:passDB@localhost/CatalogDb')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

module = Blueprint('rss_endpoints', __name__)


@module.route('/category/rss', methods=['GET'])
def categoryModel():
    try:
        categories = models.load_categories()
        if categories is None:
            abort(403)
        else:
            feed = utilities.create_feed('categories', request)
            for category in categories:
                feed.add(
                    category.id,
                    category.name,
                    id=category.id,
                    content_type='html',
                    updated=category.created_at,
                    published=category.updated_at or category.created_at)

            return feed.get_response()
    except:
        print "Unexpected error:", sys.exc_info()[0]
        print "Unexpected error:", sys.exc_info()[1]
        abort(403)


@module.route('/image/rss/id=<id>', methods = ['GET'])
def imageModel(id):
    try:
        image = models.select_image_by_id(id)
        print image
        if image is None:
            abort(403)
        else:
            feed = utilities.create_feed('image', request)
            feed.add(
                image.id,
                image.path,
                id=image.id,
                content_type='html',
                updated=image.created_at,
                published=image.updated_at or image.created_at)
            return feed.get_response()
    except:
        print "Unexpected error:", sys.exc_info()[0]
        print "Unexpected error:", sys.exc_info()[1]
        abort(403)


@module.route('/images/rss', methods = ['GET'])
@module.route('/images/rss/category_id=<category_id>', methods = ['GET'])
def imagesModel(category_id = None):
    try:
        images=None
        if (category_id is None):
            images=models.load_all_images()
        else:
            images=models.load_all_images_by_category(category_id)

        if images is None:
            abort(403)
        else:
            feed = utilities.create_feed('images', request);
            for image in images:
                feed.add(
                    image.id,
                    image.path,
                    id=image.id,
                    content_type='html',
                    updated=image.created_at,
                    published=image.updated_at or image.created_at)
            return feed.get_response()
    except:
        print "Unexpected error:", sys.exc_info()[0]
        print "Unexpected error:", sys.exc_info()[1]
        abort(403)


@module.route('/items/rss', methods = ['GET'])
@module.route('/items/rss/category_id=<category_id>', methods = ['GET'])
@module.route('/items/rss/user_id=<user_id>', methods = ['GET'])
@module.route('/items/rss/category_id=<category_id>/user_id=<user_id>', methods = ['GET'])
def itemModel(category_id = None, user_id = None):
    try:
        items=None
        if (category_id is None and user_id is None):
            items=models.select_all_items()
        elif (category_id is not None and user_id is None):
            items=models.select_items_by_category(category_id)
        elif (category_id is None and user_id is not None):
            items=models.select_items_by_user_id(user_id)
        else:
            items=models.select_items_by_user_id_and_category_id(
                user_id, category_id)

        if items is None:
            abort(403)
        else:
            feed = utilities.create_feed('items', request);
            for item in items:
                feed.add(
                    item.id,
                    item.category_id,
                    id=item.id,
                    content_type='html',
                    updated=item.created_at,
                    published=item.updated_at or item.created_at,
                    user_id=item.user_id,
                    category_id=item.category_id,
                    image_id=item.image_id)
            return feed.get_response()
    except:
        print "Unexpected error:", sys.exc_info()[0]
        print "Unexpected error:", sys.exc_info()[1]
        abort(403)
