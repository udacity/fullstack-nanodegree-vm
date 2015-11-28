#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    c = DB.cursor()
    query = "DELETE FROM matches;"
    c.execute(query)
    DB.commit()
    DB.close()

def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    query = "DELETE FROM registration; DELETE FROM players;"
    c.execute(query)
    DB.commit()
    DB.close()


def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    query = "SELECT COUNT(*) AS count FROM players"
    c.execute(query)
    result = c.fetchone()
    DB.close()
    return result[0]

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    c = DB.cursor()
    cleaned = bleach.clean(name, strip = True)
    cleaned = cleaned.replace("'", "''")
    query = "INSERT INTO players (PName) VALUES ('%s')" % (cleaned,)
    c.execute(query)
    #NEED TO ALSO REGISTER PLAYER TO TOURNAMENT via REGISTRATION table
    query = "INSERT INTO registration (PID) SELECT PID FROM players WHERE PName='%s'" % (cleaned,)
    c.execute(query)
    DB.commit()
    DB.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()
    c = DB.cursor()
    query = """SELECT p.PID, p.PName, r.Wins, r.Matches FROM players as p,
     registration as r WHERE p.PID = r.PID ORDER BY r.Matches"""
    c.execute(query)
    result = c.fetchall()
    # NEEDS A RETURN!!!!!
    DB.close()
    return result

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()
    #TODO SQL does not match code or _test
    query = "INSERT INTO matches(Winner, Loser) VALUES ('%s', '%s')" % (winner, loser)
    c.execute(query)
    DB.commit()
    DB.close()

def reportMatchDraw(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()
    query = "INSERT INTO matches(Winner, Loser, Draw) VALUES ('%s', '%s', TRUE)" % (winner, loser)
    c.execute(query)
    DB.commit()
    DB.close()
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    DB = connect()
    c = DB.cursor()
    query = ""
    c.execute(query)
    DB.close()
