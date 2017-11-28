from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Puppy(Base):
    __tablename__ = 'puppy'


    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    #Add add a decorator property to serialize data from the database

    @property
    def serialize(self):
        #returns object data in serialized format
        return {
            "name": self.name,
            "id":   self.id,
            "description": self.description
        }


engine = create_engine('sqlite:///puppies.db')
Base.metadata.create_all(engine)
