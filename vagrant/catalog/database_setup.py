import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    """docstring for User"""

    # set variable for table name
    __tablename__ = 'user'

    # create columns
    name = Column(String(80), nullable = False)
    email = Column(String(255))
    picture = Column(String(255))
    id = Column(Integer, primary_key=True)


    @property
    def serialize(self):
        """Returns object data in easily serializable format."""
        return {
            'name' : self.name,
            'email' : self.email,
            'picture' : self.picture,
            'id' : self.id
        }


class Game(Base):
    """docstring for MenuItem db"""

    # set variable for table name
    __tablename__ = 'menu_item'

    # create columns
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    category = Column(String(40))
    description = Column(String(255))
    link = Column(String(255)) # Metacritic link
    avg_rating = Column(Float)
    user_id = Column(Integer, ForeignKey('user.id'), nullable = False)

    # Set table relationships
    user = relationship(User)

    @property
    def serialize(self):
        """Returns object data in easily serializable format."""
        return {
            'name' : self.name,
            'category' : self.category,
            'description' : self.description,
            'id' : self.id,
            'link' : self.link,
            'rating' : self.rating
        }


##################### EOF code
engine = create_engine('sqlite:///favoritegames.db')

Base.metadata.create_all(engine)
##################### EOF code