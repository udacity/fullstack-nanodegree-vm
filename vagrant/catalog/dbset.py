#!/usr/bin/python

from sqlalchemy import Column, ForeignKey, Integer, String, Date, \
    Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)


class Category(Base):

    """
    Schema for category table
    """

    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    user = relationship('User')
    items = relationship('Item', backref='Category')
    user_id = Column(Integer, ForeignKey('user.id'))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""

        return {'id': self.id, 'name': self.name,
                'items': [i.serialize for i in self.items]}


class Item(Base):

    """
    Schema for item table
    """

    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(250), nullable=False)
    category = relationship('Category')
    user = relationship('User')
    category_id = Column(Integer, ForeignKey('category.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""

        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category_id': self.category_id,
            }


engine = create_engine('sqlite:///data.db')
Base.metadata.create_all(engine)
