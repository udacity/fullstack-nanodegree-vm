#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def runQuery(query):
    conn = connect()
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()

def runQueryFetch(query):
    conn = connect()
    c = conn.cursor()
    c.execute(query)
    
    outp = c.fetchall()
    conn.commit()
    conn.close()
    
    return outp

def deleteMatches():
    """Remove all the match records from the database."""
    runQuery("DELETE FROM matches;")

def deletePlayers():
    """Remove all the player records from the database."""
    runQuery("DELETE FROM players;")


def countPlayers():
    """Returns the number of players currently registered."""
    return runQueryFetch("SELECT * FROM count_players")[0][0]
    

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    runQuery("INSERT INTO players(name) VALUES('%s');" % name)


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
    return runQueryFetch("SELECT * FROM players ORDER BY wins DESC;")

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    runQuery(
        "INSERT INTO matches (player1_id, player2_id, winner_id) VALUES ({0}, {1}, {0});"
        "UPDATE players SET wins = wins + 1 WHERE id={0};"
        "UPDATE players SET matches = matches + 1 WHERE id={0};"
        "UPDATE players SET matches = matches + 1 WHERE id={1};".format(winner, loser)
    )
 
 
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

    result = []
    for i in xrange(0, countPlayers(), 2):
        query = runQueryFetch("SELECT id, name FROM players ORDER BY wins DESC LIMIT 2 OFFSET %d;" % i)
        turp = (query[0][0], query[0][1], query[1][0], query[1][1])
        result.append(turp)

    return result