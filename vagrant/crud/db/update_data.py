#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, MenuItem, Restaurant

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

result = session.query(Restaurant).filter_by(name = 'restaurant_beta').one()
result.name = 'sex'
session.add(result)
session.commit()
session.close()
