#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Restaurant, MenuItem, Base

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)

session = DBSession()
query_result = session.query(Restaurant)
menu_result = session.query(MenuItem)
restaurant = query_result.first()
menus = menu_result.all()
all = query_result.all()

for item in all:
    print item.name

session.close()
