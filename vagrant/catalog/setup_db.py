from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.reflection import Inspector

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
inspector = Inspector.from_engine(engine)

# create Session class
Session = sessionmaker(bind=engine)

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<Category(name='%s')>" % ( self.name )

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<Item(name='%s', category_id='%s')>" % ( self.name, self.category_id )


# create tables if they don't exist yet
if "categories" in inspector.get_table_names():
    Base.metadata.create_all(engine)
    session = Session()

    for category in categories:
        new_category = Category(name=category)
        session.add(new_category)
    
    session.commit()
    session.close()

# create Session instance




