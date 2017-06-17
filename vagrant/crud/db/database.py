#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)


class MenuItem(Base):
    __tablename__ = 'menu_item'
    
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(200))
    price = Column(String(8))
    course = Column(String(200))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)


engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)
