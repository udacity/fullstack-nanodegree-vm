#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach
import random


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def deleteMatches():
    """Remove all the match records from the database."""
    # connect to the database server
    connection = connect()
 
    # clean up matches table
    cursor = connection.cursor()
    cursor.execute("TRUNCATE TABLE matches;")
    
    # accept the change
    connection.commit()
    
    #close connection
    connection.close()

def deletePlayers():
    """Remove all the player records from the database."""
    # connect to the database server
    connection = connect()
 
    # execute the query
    cursor = connection.cursor()
    cursor.execute("TRUNCATE TABLE players CASCADE;")
 	
    # accept the change
    connection.commit()
    
    #close connection
    connection.close()
 


def countPlayers():
    """Returns the number of players currently registered."""
    # connect to the database server
    connection = connect()
 
    # execute the query
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM players;")
    
    # fetch results
    results = cursor.fetchone()
    
    print("Player count: %d" % results[0])

    #close connection
    connection.close()
    
    # Boolean check returns zero when results list is empty
    if not results:
    	return 0
    else:
    	return int(results[0])


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    # generate random id
    
    # connect to the database server
    connection = connect()
 
    # execute the query
    cursor = connection.cursor()
    
    cursor.execute("INSERT INTO players (player_name) VALUES (%s);", (bleach.clean(name),))
 	
 	# accept the change
    connection.commit()
    
    #close connection
    connection.close()


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
    
    # connect to the database server
    connection = connect()
    
    # execute the query into players
    cursor = connection.cursor()
    
    # execute the queries into players to get player standings
    cursor.execute("SELECT * FROM standings;")
	
    # fetch results
    results = cursor.fetchall()
    
    for result in results:
    	print("player id %s name %s wins %s matches %s " % (result[0], result[1], result[2], result[3]))
    
    #close connection
    connection.close()
    print("%d players" % len(results))
    return results


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    
    # connect to the database server
    connection = connect()
 
    # execute the query into matches
    cursor = connection.cursor()
    
    sql = "INSERT INTO matches (winner_id, loser_id) VALUES (%s, %s);"
    data = (winner, loser)
    cursor.execute(sql, data)
    
    print("winner id: %d" % winner)
    
 	# accept the change
    connection.commit()
    
    #close connection
    connection.close()
 
 
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
    
    # connect to the database server
    connection = connect()
    
    # get and store player standings
    standings = playerStandings()
    
    # execute the query
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM standings;")
    
    # fetch results
    results = cursor.fetchall()
    
    # create swiss pairings
    player = [item[0:2] for item in standings]
    
    index = 0 # our starting point
    pairings = []
    for row in results:
        while (index < row[0]):
            pair = player[index] + player[index+1] # Add two neighbors into one pair
            pairings.append(pair)
            index = index + 2 # Move our pairing cursor up by two

    #close connection
    connection.close()
    
    return pairings

