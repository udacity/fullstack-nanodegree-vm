from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, func
from passlib.apps import custom_app_context as pwd_context
from datetime import date
import uuid

# from database_setup import Base
Base = declarative_base()


class CategoryModel(Base):
    __tablename__ = 'category_table'

    id = Column(String(32), primary_key=True)
    name = Column(String(250), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        if self.updated_at is None:
            self.updated_at = self.created_at
        return {
            'name': self.name,
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }


class ImageModel(Base):
    __tablename__ = 'data_image_table'

    id = Column(String(32), primary_key=True)
    category_id = Column(String(32), ForeignKey('category_table.id'))
    path = Column(String(250), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        if self.updated_at is None:
            self.updated_at = self.created_at
        return {
            'id': self.id,
            'path': self.path,
            'category_id': self.category_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }


class UserModel(Base):
    __tablename__ = 'user_table'

    id = Column(String(32), primary_key=True)
    email = Column(String(127), nullable=False, unique=True)
    fullname = Column(String(250), nullable=True)
    picture = Column(String(250), nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        if self.updated_at is None:
            self.updated_at = self.created_at
        return {
            'id': self.id,
            'fullname': self.fullname,
            'picture': self.picture,
            'email': self.email,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }


class ItemsModel(Base):
    __tablename__ = 'items_data_table'

    id = Column(String(32), primary_key=True)
    user_id = Column(String(32), ForeignKey('user_table.id'))
    category_id = Column(String(32), ForeignKey('category_table.id'))
    image_id = Column(String(32), ForeignKey('data_image_table.id'))
    title = Column(String(250), nullable=False)
    description = Column(String(1024), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        if self.updated_at is None:
            self.updated_at = self.created_at
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'user_id': self.user_id,
            'category_id': self.category_id,
            'image_id': self.image_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }


engine = create_engine('sqlite:///udacity_catalog.db')

Base.metadata.create_all(engine)
