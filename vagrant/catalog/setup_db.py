from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

categories = [
    "Alternative",
    "Blues",
    "Acoustic Blues",
    "Children's Music",
    "Christian Gospel",
    "Classical",
    "Country",
    "Dance",
    "Easy Listening",
    "Electronic",
    "Hip Hop/Rap",
    "Holiday",
    "Industrial",
    "Jazz",
    "New Age",
    "Opera",
    "Pop",
    "R&B/Soul",
    "Reggae",
    "Rock",
    "Soundtrack",
    "World",
]

# @TODO create db if doesn't exist

Base = declarative_base()

# @TODO - disable extra logging
engine = create_engine("postgresql://vagrant:vagrant@localhost/catalog", echo=True)

# create Session class
Session = sessionmaker(bind=engine)

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    
    # @TODO - make unique
    name = Column(String)

    def __repr__(self):
        return "<Category(name='%s')>" % ( self.name )


# create tables if they don't exist yet
Base.metadata.create_all(engine) 

# create Session instance
session = Session()

for category in categories:
    new_category = Category(name=category)
    session.add(new_category)

session.commit()