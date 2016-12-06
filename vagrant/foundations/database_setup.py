
# sys module provides a number of functions and variables that can be used
# to manipulate different parts of the Python run-time environment
import sys

# import various classes from SQLAlchemy to help with writing our mapper code
from sqlalchemy import Column, ForeignKey, Integer, String

# import the declarative base which we will use in the configuration and class
# code
from sqlalchemy.ext.declarative import declarative_base

# needed for creating foreign key relationships, this will also be used
# when we write our mapper
from sqlalchemy.orm import relationship

# this will be used in the configuration code
from sqlalchemy import create_engine

# make an instance of the declarative_base class, the declarative base will
# let SQLALchemy know that our classes are special SQLAlchemy classes that
# correspond to tables in our database
Base = declarative_base()



# class code, obviously
class Restaurant(Base):
	__tablename__ = 'restaurant'

	# mapper code

	# create a name column with a max len of 80 characters and set
	# nullable equal to false which means that we cannot create a row
	# if this value is not filled out
	name = Column(String(80), nullable = False)

	# create an id column that holds an integer and indicate that it is
	# a primary key
	id = Column(Integer, primary_key = True)

class MenuItem(Base):
	__tablename__ = 'menu_item'

	# mapper code, which maps variables that we create to columns in
	# our tables in the database

	name = Column(String(80), nullable = False)

	id = Column(Integer, primary_key = True)

	course = Column(String(250))

	description = Column(String(250))

	price = Column(String(8))

	# specify foreign key, this says, look inside the restaurant table,
	# and look for the id column whenever I ask for restaurant_id
	restaurant_id = Column(Integer, ForeignKey('restaurant.id'))

	# this is a feature of the ORM and tells it that the two classes
	# are related in the same way that setting up the foreign key relationship
	# tells SQL that the tables are related. It's smart enough to figure out
	# what kind of relationship it is based on how we set up the foreign key
	restaurant = relationship(Restaurant)

# Insert at end of file

# create instance of create_engine class and point to the database we will use
# I believe this also creates that file restaurantmenu.db too
# it looks like this will be needed everytime you want to connect to the DB
# too, since it will form the connection with the DB-API
engine = create_engine('sqlite:///restaurantmenu.db')

# this goes into the db and adds the classes we will soon create as
# new tables in our database
Base.metadata.create_all(engine)