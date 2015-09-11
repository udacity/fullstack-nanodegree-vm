#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

# Runs a query
def runQuery(query):
    if type(query) is list:
        if len(query) >= 3:
            raise ValueError('Query can only contain up to 2 arguments')
    
    conn = connect()
    c = conn.cursor()
    if type(query) is str: # If query is just a string
        c.execute(query)
    else: # If it's an array, pass second param as data
        c.execute(query[0], query[1])
    conn.commit()
    conn.close()

# Runs a query and gets a result
def runQueryFetch(query):
    if type(query) is list:
        if len(query) >= 3:
            raise ValueError('Query can only contain up to 2 arguments')
            
    conn = connect()
    c = conn.cursor()
    if type(query) is str: # If query is just a string
        c.execute(query)
    else: # If it's an array, pass second param as data
        c.execute(query[0], query[1])
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
    runQuery(["INSERT INTO players(name) VALUES(%s);", (name, )])


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
    
    runQuery([
        "INSERT INTO matches (player1_id, player2_id) VALUES (%s, %s);"
        "UPDATE players SET wins = wins + 1 WHERE id=%s;"
        "UPDATE players SET matches = matches + 1 WHERE id=%s;"
        "UPDATE players SET matches = matches + 1 WHERE id=%s;",
        (winner, loser, winner, loser, winner)
    ])
 
 
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
    # Loop through every 2 players
    for i in xrange(0, countPlayers(), 2):
        # Get next 2 players
        query = runQueryFetch(["SELECT id, name FROM players ORDER BY wins DESC LIMIT 2 OFFSET %s;", (i, )])
        turp = (query[0][0], query[0][1], query[1][0], query[1][1]) # Add both players to turple
        result.append(turp) # Add turple to list

    return result