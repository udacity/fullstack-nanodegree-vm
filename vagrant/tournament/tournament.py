#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def singleQuery(query):
    conn = connect()
    curr = conn.cursor()
    curr.execute(query)
    conn.commit()
    curr.close()
    conn.close()

def returnQuery(query):
    conn = connect()
    curr = conn.cursor()
    curr.execute(query)
    singleResult = curr.fetchone()[0]
    conn.commit()
    curr.close()
    conn.close()
    return singleResult

def multiQuery(query):
    conn = connect()
    curr = conn.cursor()
    curr.execute(query)
    multiResult = curr.fetchall()
    conn.commit()
    curr.close()
    conn.close()
    return multiResult

def singleInsert(query, value):
    conn = connect()
    curr = conn.cursor()
    #print curr.mogrify("INSERT INTO players (player_name) VALUES (%s);", (name))
    curr.execute(query, (value,))
    conn.commit()
    curr.close()
    conn.close()

def deleteMatches():
    """Remove all the match records from the database."""
    #Delete the records from all tables which have records of matches or results
    query = "DELETE from matches;"
    singleQuery(query)

def deletePlayers():
    """Remove all the player records from the database."""
    #Delete the player records - cascades in place to ensure correct execution.
    query = "DELETE from players;"
    singleQuery(query)

def countPlayers():
    """Returns the number of players currently registered."""
    #Need to examine this code to see if it can be executed more efficiently.
    query = "SELECT count(*) from players;"
    return returnQuery(query)


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
        #Insert the player name, no need to return anything
    query = "INSERT INTO players (player_name) VALUES (%s);"
    singleInsert(query, name)



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
    #Return players and standings
    query = "SELECT * FROM playerStandings;"
    return multiQuery(query)


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    query = "INSERT INTO matches (winner_id, loser_id) VALUES %s;"
    singleInsert(query, (winner, loser),)
    query = "UPDATE playerScore SET matches = matches + 1 WHERE player_id IN %s;"
    singleInsert(query, (winner, loser),)
    query = "UPDATE playerScore SET score = score + 1 WHERE player_id IN (%s);"
    singleInsert(query, (winner),)

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
    players = playerStandings()
    print players
