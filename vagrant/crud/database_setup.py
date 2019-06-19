import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurant'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)


class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

if __name__ == '__main__':
    engine = create_engine('sqlite:///restaurantmenu.db')
    Base.metadata.create_all(engine)
    DBSession = sessionmaker(bind = engine)
    session = DBSession()
    restaurant_list = [
        'Pizza Palace',
        'Pizza Hut',
        'Clover',
        'The Pajer Don Pancho',
        'El costumbrista',
        'Pizza el Padrino'
    ]
    for restaurant in restaurant_list:
        restaurant_object = Restaurant(name=restaurant)
        session.add(restaurant_object)
    session.commit()
    session.query(Restaurant).all()
