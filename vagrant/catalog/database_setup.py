import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()

class User(Base):
    """Table for Users"""

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
        games = Game.get_games_by_id(self.id)
        return {
            'name' : self.name,
            'email' : self.email,
            'picture' : self.picture,
            'id' : self.id,
            'games' : games
        }


class Game(Base):
    """Table for individual games."""

    # set variable for table name
    __tablename__ = 'game'

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

    @classmethod
    def get_games_by_id(cls, id_list):
        """
        Returns the games with the given ids.

        >>>get_games_by_id((1,2,3))
        Mass Effect, Nioh, Tomb Raider
        """
        games = []

        for id in id_list:
            game = session.query(cls).filter_by(id = id).one()
            games.append(game)

        return games

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


class UsersGames(Base):
    """Table for storing User's favorite games."""

    # set variable for table name
    __tablename__ = 'usersgames'


    # create columns
    user_id = Column(Integer, ForeignKey('user.id'), nullable = False)
    game_id = Column(Integer, ForeignKey('game.id'), nullable = False)

    # set table relationships
    user = relationship(User)
    game = relationship(Game)

    @classmethod
    def get_users_games(cls, user_id):
        """Returns a list of games for the given user_id."""
        return session.query(cls).filter_by(user_id = user_id).all()

        


##################### EOF code
engine = create_engine('sqlite:///favoritegames.db')

Base.metadata.create_all(engine)

# Create database connector
DBSession = sessionmaker(bind = engine)
session = DBSession()
##################### EOF code