import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

# @TODO - disable extra logging
engine = create_engine("postgresql://vagrant:vagrant@localhost/catalog", echo=True)

# create Session class
DBSession = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    picture = Column(Text)

    def __repr__(self):
        return "<User(name='%s', email='%s', picture='%s')>" % ( self.name, self.email, self.picture )

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    items = relationship('Item', backref="items")

    def __repr__(self):
        return "<Category(name='%s')>" % ( self.name )

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    category = relationship('Category', backref="categories")
    name = Column(String, nullable=False)
    description = Column(Text);
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<Item(name='%s', category_id='%s')>" % ( self.name, self.category_id )
