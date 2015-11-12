from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
# import psycopg2

Base = declarative_base()

engine = create_engine('sqlite:///udacity_catalog.db')
# engine = create_engine('postgresql:////localhost//udacity_catalog_db')


Base.metadata.create_all(engine)
