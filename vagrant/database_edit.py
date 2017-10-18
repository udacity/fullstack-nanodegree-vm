from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_initial import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

veggieBurgers = session.query(MenuItem).filter_by(name='Veggie Burger')
for veggieBurger in veggieBurgers:
    print(veggieBurger.id)
    print(veggieBurger.price)
    print(veggieBurger.restaurant.name)
    print("\n")

# UrbanVeggieBurger = session.query(MenuItem).filter_by(id=8).one()
# UrbanVeggieBurger.price = '$2.99'
# session.add(UrbanVeggieBurger)
# session.commit()
# print(UrbanVeggieBurger.price)
#
# spinach = session.query(MenuItem).filter_by(name='Spinach Ice Cream').one()
# print(spinach.id)
# print(spinach.price)
# print(spinach.restaurant.name)
# session.delete(spinach)
# session.commit()
