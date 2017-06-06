import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    """docstring for User"""

    # set variable for table name
    __tablename__ = 'user'

    # create columns
    name = Column(String(80), nullable = False)
    email = Column(String(255))
    picture = Column(String(255))
    id = Column(Integer, primary_key=True)


    @property
    def serialize(self):
        """Returns object data in easily serializable format."""
        return {
            'name' : self.name,
            'email' : self.email,
            'picture' : self.picture,
            'id' : self.id
        }
        

class Restaurant(Base):
    """docstring for Restuarant db"""
    
    # set variable for table name
    __tablename__ = 'restaurant'

    # create columns
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))

    # Set table relationships
    user = relationship(User)

    @property
    def serialize(self):
        """Returns object data in easily serializable format."""
        return {
            'name' : self.name,
            'id' : self.id
        }


class MenuItem(Base):
    """docstring for MenuItem db"""

    # set variable for table name
    __tablename__ = 'menu_item'

    # create columns
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

    # Set table relationships
    restaurant = relationship(Restaurant)
    user = relationship(User)

    @property
    def serialize(self):
        """Returns object data in easily serializable format."""
        return {
            'name' : self.name,
            'description' : self.description,
            'id' : self.id,
            'price' : self.price,
            'course' : self.course
        }




##################### EOF code
engine = create_engine('sqlite:///restaurantmenuwithusers.db')

Base.metadata.create_all(engine)
##################### EOF code