#creating objects to add to the table
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
myFirstRestaurant = Restaurant(name="Casa da Carne")
session.add(myFirstRestaurant)
session.commit()

session.query(Restaurant).all()
firstResult = session.query(Restaurant).first()
print firstResult.name

myFirstMenuItem = MenuItem(name="Costela", description="Carne de costela blablablabl")
session.add(myFirstMenuItem)
session.commit()
firstResult = session.query(MenuItem).first()
print firstResult.name

