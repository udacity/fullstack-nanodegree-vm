from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base,Restaurant,MenuItem
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
updateRestaurant = session.query(Restaurant).filter_by(id=1).one()
updateRestaurant.name='Khan and Singh'
session.add(updateRestaurant)
session.commit()