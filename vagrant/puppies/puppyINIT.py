
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from puppies import Base, Shelter, Puppy
#from flask.ext.sqlalchemy import SQLAlchemy
from random import randint
import datetime

def sess():
    engine = create_engine('sqlite:///puppyshelter.db')

    Base.metadata.bind = engine
    
    DBSession = sessionmaker(bind=engine)

    return DBSession()