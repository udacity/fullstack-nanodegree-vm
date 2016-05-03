#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#
import psycopg2
from psycopg2._psycopg import Error, Warning, DataError, DatabaseError, ProgrammingError
import psycopg2.extensions
import itertools
    

def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    # We make use of the connect() method so that we could avoid the code repetition.
    # We can refactor our connect() method to deal not only with the database connection
    # but also with the cursor since we can assign and return multiple variables simultaneously.
    # In the stage of setting up the connection with the DB, sometimes we may encounter different exceptions.
    # In practice, we handle this crucial stage carefully by using try/except block.
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        raise IOError("Connected!\n")
    
def deleteMatches():
    """Remove all the match records from the database."""
    db, cursor = connect()
    cursor = db.cursor()
    
    query = "TRUNCATE matches;"
    cursor.execute(query)

    db.commit()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""
    query = "DELETE FROM players;"
    cursor.execute(query)

    db.commit()
    db.close()

def countPlayers():
    """Returns the number of players currently registered."""
    query = "SELECT count(*) AS num FROM players;"
    cursor.execute(query)
    count = cursor.fetchone()[0]

    db.close()
    return count

def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player. (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
    name: the player's full name (need not be unique).
    """
    query = "INSERT INTO players (name) VALUES (%s);"
    parameter = (name,)
    cursor.execute(query, parameter)

    db.commit()
    db.close()
    
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
    cursor.execute("SELECT * FROM standings ORDER BY wins DESC;")
    playerslist = cursor.fetchall() # Fetches all remaining rows of a query result, returning a list.

    db.close()
    return playerslist

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Args:
    winner: the id number of the player who won
    loser: the id number of the player who lost
    """
    query = "INSERT INTO matches (winner, loser) VALUES (%s, %s);"
    parameter = (winner, loser)
    cursor.execute(query, parameter)

    db.commit()
    db.close()

def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2),
      first player's unique id
      name1: the first player's name
      id2: the second player's unique id
      name2: the second player's name
    """
    # For swissPairings consulted GitHub, Stack OverFlow
    # and the recipes section of Python's
    # itertools docs: https://docs.python.org/2/library/itertools.html
    # and the Python Standard Library.

    # Iterate through the list and build the pairings to return results
    results = []
    pair = []
    standings = playerStandings()
    # standings = [(id1, name1, wins1, matches1), (id2, name2, wins2, matches2)]
    # [id1, id2, id3, id4, id5, id6, id7, id8] = [row[0] for row in standings]
    # pairings = swissPairings()
    pairingsiterator = itertools.izip(*[iter(standings)]*2)
    pairings = list(pairingsiterator)
    for pair in pairings:
        id1 = pair[0][0]
        name1 = pair[0][1]
        id2 = pair[1][0]
        name2 = pair[1][1]
        matchup = (id1, name1, id2, name2)
        results.append(matchup)
    return results
