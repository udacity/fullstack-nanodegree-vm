import sys  # used to manipulate different parts of the python run-time environment
from sqlalchemy import Column, ForeignKey, Integer, String  # used in the part of mapper code
from sqlalchemy.ext.declarative import declarative_base  # used in the part of configuration and class code
from sqlalchemy.orm import relationship  # for creating our foreign key relationships
from sqlalchemy import create_engine  # used in the part of configuration code at the end of the file

Base = declarative_base()  # let SQLAlchemy know that our classes are special SQLAlchemy classes


class Restaurant(Base):
    __tablename__ = 'restaurant'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)


class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))

    restaurant = relationship(Restaurant)


    # serialize function allows us to send JSON objects in a serializable format
    @property
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
        }


################################# insert at end of file #################################

# create a new file that we can use similarly to a more robust database like MySQL (SQLiete)
engine = create_engine('sqlite:///restaurantmenu.db')  # point to the database we use

Base.metadata.create_all(engine)  # go into the database and add the classes we create as new tables in our database


