from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# @TODO - disable extra logging
engine = create_engine("postgresql://vagrant:vagrant@localhost/catalog", echo=True)

# create Session class
DBSession = sessionmaker(bind=engine)

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<Category(name='%s')>" % ( self.name )

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    name = Column(String)

    def __repr__(self):
        return "<Item(name='%s', category_id='%s')>" % ( self.name, self.category_id )
