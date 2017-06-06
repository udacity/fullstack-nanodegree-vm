import sys

from time import mktime

from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
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
        unjson_ratings = UsersGames.get_games_by_user_id(self.id)

        if unjson_ratings:
            ratings = [rating.serialize for rating in unjson_ratings]
        else:
            ratings = "No ratings"

        return {
            'name' : self.name,
            'email' : self.email,
            'picture' : self.picture,
            'id' : self.id,
            'ratings' : ratings
        }


class Game(Base):
    """Table for individual games."""

    # set variable for table name
    __tablename__ = 'game'

    # create columns
    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    category = Column(String(40))
    description = Column(String(1020))
    avg_rating = Column(Float)
    modified = Column(DateTime)

    @classmethod
    def get_games_by_id(cls, id_list):
        """
        Returns the games with the given ids.

        >>>get_games_by_id((1, 2, 3))
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
            'id' : self.id,
            'category' : self.category,
            'avg_rating' : self.avg_rating,
            'description' : self.description,
            'last modified' : int(mktime(self.modified.timetuple()))
        }


class UsersGames(Base):
    """Table for storing User's favorite games."""

    # set variable for table name
    __tablename__ = 'usersgames'


    # create columns
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable = False)
    game_id = Column(Integer, ForeignKey('game.id'), nullable = False)
    rating = Column(Integer)
    modified = Column(DateTime)

    # set table relationships
    user = relationship(User)
    game = relationship(Game)

    @classmethod
    def get_games_by_user_id(cls, user_id):
        """
        Returns a list of games for the given user_id.

        >>> get_users_games(1)
        (Mass Effect, Nioh, Tomb Raider)
        """
        return session.query(cls).filter_by(user_id = user_id).all()

    @classmethod
    def get_users_by_game_id(cls, game_id):
        """
        Return a list of user_ids for the given game.

        >>> get_games_users(1)
        (32, 24, 6)
        """
        return session.query(cls).filter_by(game_id = game_id).all()

    @property
    def serialize(self):
        """Returns object data in easily serializable format."""
        return {
            'id' : self.id,
            'user_id' : self.user_id,
            'game_id' : self.game_id,
            'last modified' : int(mktime(self.modified.timetuple())),
            'rating' : self.rating
        }

        


##################### EOF code
engine = create_engine('sqlite:///favoritegames.db')

Base.metadata.create_all(engine)

# Create database connector
DBSession = sessionmaker(bind = engine)
session = DBSession()
##################### EOF code