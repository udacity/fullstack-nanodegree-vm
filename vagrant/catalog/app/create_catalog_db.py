from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json
import re
import uuid
import base64
# from datetime import date
# from database_setup import Restaurant, Base, MenuItem
# from database_setup import Base

from models import Base, CategoryModel, ImageModel, UserModel, ItemsModel

# engine = create_engine('postgresql:////localhost//udacity_catalog_db')
engine = create_engine('sqlite:///udacity_catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

categories = ['Soccer', 'Basketball', 'Baseball', 'Frisbee', 'Snowboarding',
              'Rock Climbing', 'Foosball', 'Ski', 'Hockey', 'La Crosse', 'Football']
categories_id = {}

for name in categories:
    id = re.sub(r"[+=\/]", "_", base64.b64encode(uuid.uuid4().bytes))
    category = CategoryModel(id=id, name=name)
    categories_id[name] = id
    session.add(category)
    session.commit()

print "done with catalog!!!"

with open('data_image.json') as data_file:
    data = json.load(data_file)

for name in categories:
    for key in data[name]:
        image_data = json.loads(json.dumps(
            key, ensure_ascii=False).decode('utf8'))
        for id in image_data:
            file_path = image_data[id]
            category_id = categories_id[name]
            image_model = ImageModel(
                id=id, path=file_path, category_id=category_id)
            session.add(image_model)
            session.commit()
print "done with image!!!"

user_model = UserModel(fullname='Stanley Calixte',
                       picture='https://lh3.googleusercontent.com/-XdUIqdMkCWA/AAAAAAAAAAI/AAAAAAAAAAA/4252rscbv5M/photo.jpg',
                       email='scalixte@gmail.com',
                       id=re.sub(r"[+=\/]", "_", base64.b64encode(uuid.uuid4().bytes)))
session.add(user_model)
session.commit()
print "done with new user!!!"

with open('data_items.json') as data_file:
    item_data = json.load(data_file)

for name in categories:
    for item in item_data[name]:
        item_model = ItemsModel(
            id=re.sub(r"[+=\/]", "_", base64.b64encode(uuid.uuid4().bytes)),
            title=item['title'],
            description=item['description'],
            image_id=item['image_id'],
            category_id=categories_id[name],
            user_id=user_model.id
        )
        session.add(item_model)
        session.commit()

print "done with items creation!!!"
