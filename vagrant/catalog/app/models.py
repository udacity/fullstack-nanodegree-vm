from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    picture = Column(String(250))


class Category(Base):

    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(250), nullable=True)
    items = relationship("Item", backref="Category")

    def __init__(self, name, description):
        self.name = name
        self.description = description


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(250), nullable=False)
    image_name = Column(String(250), nullable=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category')

    def __init__(self, name, description, image_name, category_id):
        self.name = name
        self.description = description
        self.image_name = image_name
        self.category_id = category_id
