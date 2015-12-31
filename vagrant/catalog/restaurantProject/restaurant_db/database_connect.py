#connection to the db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurant_db.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

firstResult = session.query(Restaurant).first()
print firstResult.name + "\n\n\n"

dummy = Restaurant(name="dummy")

allRestaurants = dummy.listAll(session)

print "\n\n\n Found" + str(allRestaurants.__len__()) +" Restaurants in town: \n"

for item in allRestaurants:
    print item.name + " " + str(item.id)
