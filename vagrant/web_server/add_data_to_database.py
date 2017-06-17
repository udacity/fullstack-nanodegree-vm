#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, Restaurant

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

def add_restaurant(name):
    restaurant_name = Restaurant(name = name)
    session.add(restaurant_name)
    session.commit()
    print('Adding Success: %s' % name)

if __name__ == '__main__':
    add_restaurant('Verb')
    add_restaurant('Uber')
    add_restaurant('T')
