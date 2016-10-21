#configuration
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


# Users
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


# Parks
class Parks(Base):
    __tablename__ = 'parks'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lat = Column(Integer)
    lon = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)

    @property 
    def serialize(self):
        #returns data in serializable format
        return {
            'id' : self.id,
            'name' : self.name,
            'lat' : self.lat,
            'lon' : self.lon
        }


#Trails
class Trails(Base):

    #table
    __tablename__ = 'trails'

    #rows
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    park_id = Column(Integer, ForeignKey('parks.id'))
    park = relationship(Parks)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)

    @property
    def serialize(self):
        #returns data in serializable format
        return {
            'id' : self.id,
            'name' : self.name,
            'park' : self.park_id
        }





#######insert at end of file #########
engine = create_engine('sqlite:///chisel.db')

Base.metadata.create_all(engine)