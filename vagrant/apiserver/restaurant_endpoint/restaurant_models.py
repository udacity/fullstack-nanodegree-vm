# -*- coding: utf-8 -*-
from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine





Base = declarative_base()
class Restaurant(Base):
  __tablename__ = 'restaurant'
  id = Column(Integer, primary_key = True)
  restaurant_name = Column(String)
  restaurant_address = Column(String)
  restaurant_image = Column(String)
  
  
  #Add a property decorator to serialize information from this database
  @property
  def serialize(self):
    return {
      'restaurant_name': self.restaurant_name,
      'restaurant_address': self.restaurant_address,
      'restaurant_image' : self.restaurant_image,
      'id' : self.id
      
      }

engine = create_engine('sqlite:///restaruants.db')
 

Base.metadata.create_all(engine)