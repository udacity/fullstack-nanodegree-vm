#database setup file
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

#Class setup
class Shelter(Base):
    __tablename__ = 'shelter'
    name = Column(String(80), nullable=False)
    address = Column(String(250))
    city = Column(String(60))
    state = Column(String(60))
    zipCode = Column(String(15))
    website = Column(String(250))
    id = Column(Integer, primary_key=True)
	
class Puppy(Base):
    __tablename__ = 'puppy'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    dateOfBirth = Column(Date)
    picture = Column(String)
    gender = Column(String(6), nullable=False)
    weight = Column(Float(precision=2))
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)



#insert at end of file

engine = create_engine('sqlite:///puppyshelter2.db')

Base.metadata.create_all(engine)
