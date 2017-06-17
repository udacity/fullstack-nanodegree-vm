#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, Restaurant

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

def query_data_from_restaurant():
    result = session.query(Restaurant).all()

    for item in result:
        print(item.name)


if __name__ == '__main__':
    query_data_from_restaurant()
