import os
import sys
import json
import re
import uuid
import base64
from datetime import date, datetime
import traceback
import subprocess
from functools import wraps

from flask import current_app as app


from data_models import Base, CategoryModel, ImageModel, UserModel, ItemsModel

from sqlalchemy import create_engine, desc, func
from sqlalchemy.orm import sessionmaker, outerjoin
from flask import current_app as app

engine = create_engine('postgresql://catalog:passDB@localhost/CatalogDb')


Base.metadata.bind = engine
DBsession = sessionmaker(bind=engine)
session = DBsession()


def commit_and_close(f):
    @wraps(f)
    def session_functions(*args, **kwargs):
        session = DBsession()
        res = f(*args, **kwargs)
        session.close()
        return res
    return session_functions


@commit_and_close
def insert_to_category(id, name):
    category = CategoryModel(id=id, name=name)
    session.add(category)
    session.commit()
    session.refresh(category)
    return category


@commit_and_close
def load_categories():
    return session.query(CategoryModel).all()


@commit_and_close
def insert_image(id, file_path, category_id):
    image = ImageModel(id=id, path=file_path, category_id=category_id)
    session.add(image)
    session.commit()
    session.refresh(image)
    return image


@commit_and_close
def select_image_by_id(id):
    return session.query(ImageModel).filter_by(id=id).scalar()


@commit_and_close
def load_all_images():
    return session.query(ImageModel).all()


@commit_and_close
def load_all_images_by_category(category_id):
    return session.query(ImageModel).filter_by(category_id=category_id).all()


@commit_and_close
def insert_new_user(fullname, email, picture):
    user_model = UserModel(fullname=fullname, email=email, picture=picture,
                           id=re.sub(r"[+=\/]", "_", base64.b64encode(uuid.uuid4().bytes)))
    session.add(user_model)
    session.commit()
    session.refresh(user_model)
    return user_model


@commit_and_close
def select_user_by_email(email):
    return session.query(UserModel).filter_by(email=email).scalar()

@commit_and_close
def select_all_users():
    return session.query(UserModel).all()

@commit_and_close
def insert_new_item(user_id, title, description, category_id, image_id):
    item_model = ItemsModel(
        id=re.sub(r"[+=\/]", "_", base64.b64encode(uuid.uuid4().bytes)),
        title=title,
        description=description,
        image_id=image_id,
        category_id=category_id,
        user_id=user_id
    )
    session.add(item_model)
    session.commit()
    session.refresh(item_model)
    return item_model


@commit_and_close
def select_all_items():
    return session.query(ItemsModel).all()


@commit_and_close
def select_items_by_category(category_id):
    return session.query(ItemsModel).filter_by(category_id=category_id).all()


@commit_and_close
def select_items_by_user_id(user_id):
    return session.query(ItemsModel).filter_by(user_id=user_id).all()


@commit_and_close
def select_items_by_user_id_and_category_id(user_id, category_id):
    return session.query(ItemsModel).filter_by(
        user_id=user_id, category_id=catalog_id).all()


@commit_and_close
def select_item_by_id(id):
    return session.query(ItemsModel).filter_by(id=id).scalar()


@commit_and_close
def delete_item(itemToDelete):
    session.delete(itemToDelete)
    session.commit()


@commit_and_close
def update_item(item, title, description, image_id, category_id):
    item.title = title
    item.description = description
    item.image_id = image_id
    item.category_id = category_id
    item.updated_time = datetime.now()
    session.commit()
