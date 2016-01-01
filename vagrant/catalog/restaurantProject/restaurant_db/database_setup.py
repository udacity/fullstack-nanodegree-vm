import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    def find(self, session):
        item = session.query(Restaurant).filter_by(name = self.name).first()
        return item

    def listAll(self, session, name_order):
        if name_order ==False:
            items = session.query(Restaurant).all()
        else:
            items = session.query(Restaurant).order_by(Restaurant.name).all()
        return items

    def add (self, session):
        session.add(self)
        session.commit()

    def remove(self, session):
        session.delete(self)
        session.commit()

    def update(self, session, new_name):
        self.name = new_name
        session.add(self)
        session.commit()



class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)


engine = create_engine('sqlite:///restaurant_db.db')


Base.metadata.create_all(engine)
