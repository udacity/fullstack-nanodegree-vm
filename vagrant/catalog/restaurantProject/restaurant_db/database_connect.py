#connection to the db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
"""
engine = create_engine('sqlite:///restaurant_db.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
"""
#firstResult = session.query(Restaurant).first()
#print firstResult.name + "\n\n\n"

def Restaurant_list():
    #coneecting DB for query
    engine = create_engine('sqlite:///restaurant_db.db')
    Base.metadata.bind=engine
    DBSession = sessionmaker(bind = engine)
    session = DBSession()
    dummy = Restaurant(name="dummy")
    allRestaurants = dummy.listAll(session)
    return allRestaurants
