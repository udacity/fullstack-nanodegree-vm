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
    commit('update players set matches = 0, rank = 0;')


def deletePlayers():
    """Remove all the player records from the database."""
    commit('delete from players;')


def countPlayers():
    """Returns the number of players currently registered."""
    count = select('select count(*) as num from players;')[0][0]
    return count


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """

    conn = connect()
    c = conn.cursor()
    c.execute("insert into players (name, rank, matches) values (%s, 0, 0)", (name,))
    conn.commit() 
    conn.close()


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
    query = select('select * from players order by rank')
    return query


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    #get winners rank, add 1, then store back
    conn = connect()
    c = conn.cursor()
    c.execute("update players set matches = matches + 1, rank = rank + 1 where id = %s", (winner,))
    conn.commit()
    conn.close()

    #increment losers matches but not wins(rank)
    conn = connect()
    c = conn.cursor()
    c.execute("update players set matches = matches + 1 where id = %s", (loser,))
    conn.commit()
    conn.close()
 
 
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

    lineup = []
    players = select("select id, name from players order by rank desc")
    for x in range(0, countPlayers(), 2):
        lineup.append((players[x][0], players[x][1], players[x+1][0], players[x+1][1]))
    #print lineup #debugging
    return lineup

#used for simplifying code for simple executions to the database
def commit(sql):
    conn = connect()
    c = conn.cursor()
    c.execute(sql)
    conn.commit() 
    conn.close()

#used for simplifying code for simple select queries 
def select(sql):
    conn = connect()
    c = conn.cursor()
    c.execute(sql)
    val = c.fetchall() 
    conn.close()
    return val
