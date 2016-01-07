"""
this is the setup file for my database
Author: Bret Wagner

"""

import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()
##### Code above this is for setting up sqlalchemy and python #####

# setup classes(tables) to be used in the database
class Restaurant(Base):
    """
    This will contain the restaurants table
    for the database
    """
    __tablename__ = 'restaurants'
    # Declare columns and purposes/keys etc.
    name = Column(
        String(80), nullable = False)
    id = Column(
        Integer, primary_key = True)

class MenuItem(Base):
    """
    This will contain the Menu items table
    for the database
    """
    __tablename__ = 'menu_item'
    # Declare columns and purposes/keys/etc.
    name = Column(
        String(80), nullable = False)
    id = Column(
        Integer, primary_key = True)
    description = Column(
        String(255))
    price = Column(
        String(10), nullable = False)
    course = Column(
        String(16))
    restaurant_id = Column(
        Integer, ForeignKey('restaurants.id'))
    restaurant = relationship(Restaurant)
    
    
##### keep code above this line #####
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)