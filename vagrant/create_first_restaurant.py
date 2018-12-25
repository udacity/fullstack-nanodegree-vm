from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurant_menu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

# empty all rows of Restaurant and MenuItem
session.query(Restaurant).delete()
session.query(MenuItem).delete()

# add new row in Restaurant
restaurant1 = Restaurant(name = 'Mister Pogi')
session.add(restaurant1)
session.commit()

# query all rows of Restaurant
print(session.query(Restaurant).all())

# add new row in MenuItem
menu_item1 = MenuItem(
    name = 'Cheeze Pizza',
    description = 'Made with all natural ingredients and fresh mozarella.',
    course = 'Entree',
    price = '$8.99',
    restaurant = restaurant1)
session.add(menu_item1)
session.commit()

# query all rows of MenuItem
print(session.query(MenuItem).all())

first_restaurant = session.query(Restaurant).first()
print(first_restaurant.name)

first_menu_item = session.query(MenuItem).first()
print(first_menu_item.name)
print(first_menu_item.restaurant.name)

# restaurants = session.query(Restaurant).all()
# for restaurant in restaurants:
#     print(restaurant.name)