from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    picture = Column(String(250))


class Category(Base):

    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False, unique=True)
    description = Column(String(250), nullable=True)
    items = relationship("Item", backref="Category")
    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship('User')

    def __init__(self, name, description, author_id):
        self.name = name
        self.description = description
        self.author_id = author_id

    @property
    def to_json(self):
        category = {"name": self.name,
                    "description": self.description,
                    "id": self.id
                    }
        category['items'] = [i.to_json for i in self.items]
        return category


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False, unique=True)
    description = Column(String(250), nullable=True)
    image_name = Column(String(250), nullable=False, default='no-image-large.png')
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category')
    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship('User')

    def __init__(self, name, description, category_id, author_id):
        self.name = name
        self.description = description
        self.category_id = category_id
        self.author_id = author_id

    @property
    def to_json(self):
        return {"id": self.id,
                "name": self.name,
                "description": self.description,
                "image_name": self.image_name,
                "category_id": self.category_id
                }
