# import dependencies
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# create an instance of the engine class and tell it to use our
# restaurant db
engine = create_engine('sqlite:///restaurantmenu.db')

# bind the engine to the base class
Base.metadata.bind = engine

# this makes the connections between our class definitions and the corresponding
# tables within our database

# make a session maker object
DBSession = sessionmaker(bind = engine)

# make a session with the session maker, this session will be
# like our git staging area
session = DBSession()

# now we can add stuff

# create a new Restaurant instance
newRestaurant = Restaurant(name = 'Canalis')

# add it to the staging area
session.add(newRestaurant)

# add it to the DB with commit
session.commit()


