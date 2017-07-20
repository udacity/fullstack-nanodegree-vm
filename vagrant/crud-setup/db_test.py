from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)

session = DBSession()


urbanVeggieBurger = session.query(MenuItem).filter_by(name = 'Veggie Burger')
for uvb in urbanVeggieBurger:
	if uvb.price != '2.99$':
		uvb.price = '2.99$'
		session.add(uvb)
		session.commit()

veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
for vb in veggieBurgers:
	print vb.id
	print vb.name
	print vb.price
	print vb.restaurant.name
	print "\n"
