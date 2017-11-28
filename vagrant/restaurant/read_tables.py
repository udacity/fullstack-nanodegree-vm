from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base,Restaurant,MenuItem
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
MenuData = session.query(MenuItem).filter(MenuItem.id < 11).all()
for menu in MenuData:
	print menu.id,menu.name,menu.description,menu.price,menu.course

firstMenuItem= session.query(MenuItem).first()	
print firstMenuItem.id, firstMenuItem.name,firstMenuItem.price