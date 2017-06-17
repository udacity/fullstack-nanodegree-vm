#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
