from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBsession = sessionmaker(bind = engine)
sess = DBsession()
myFirstRestaurant = Restaurant(name = "Pizza Palace")
sess.add(myFirstRestaurant)
sess.commit()
cheesepizza = MenuItem(name = "Cheese Pizza", price = "$2.99", restaurant = myFirstRestaurant)
sess.add(cheesepizza)
sess.commit()
