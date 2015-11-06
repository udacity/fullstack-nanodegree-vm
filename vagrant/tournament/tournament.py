#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


# Declare global variables here to be used across functions
psql = psycopg2
conn = psql.connect("dbname='tournament'")
cur = conn.cursor()
num = int

"""
##############################
# Test Code block
# execute SQL command, Return one result
try:
    cur.execute("select * from players")
    output = cur.fetchall()
    print output
except:
    print "unable to print output"
    

# End Test Code Block
##############################
"""
# Declare funtions to be used in applications of the database
def getID():
    """use SQL to create a custom ID """
    cur.execute("select md5(random()::text || clock_timestamp()::text)::uuid")
    output = cur.fetchone()
    return output

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection.
    check if database tournament exists
    else create
    """
    return psycopg2.connect("dbname='tournament'")
    

def deleteMatches():
    """Remove all the match records from the database.
    delete * from matches;
    """
    cur.execute("delete from matches where mID != 0")
    conn.commit()


def deletePlayers():
    """Remove all the player records from the database.
    delete * from players;
    """
    cur.execute("delete from players where PlayerID > 0")
    conn.commit()
    


def countPlayers():
    """Returns the number of players currently registered.
    select count(*) from players
    """
    cur.execute("""SELECT COUNT(*) FROM players""")
    output = cur.fetchone()
    return output[0]
    
    

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    # validate name for '
    if '\'' in name:
        name_part = name.split('\'')
        print name_part
        name = name_part[0]+'\'\''+name_part[1]
        print name
    cur.execute("insert into players (name) values ('"+name+"')")
    
    conn.commit                

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.
    
    slect LastName, FirstName, Rank, Wins, matches order by rank desc

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    cur.execute("select PlayerID, name, Wins, Matches from players where PlayerID != 0")
    output = cur.fetchall()
    return output

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
      
      get current win count
      add new win
      display output
    """
    # get current wins of winners
    cur.execute("select name, wins from players")
    output = cur.fetchall()
    print output
    """
    cur.execute("select name from players where PlayerID = "+ str(winner))
    output=cur.fetchall()
    print output
    """
    

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

    
"""
##############################
# Test Code block
# execute SQL command, Return one result
try:
    cur.execute("select * from players")
    output = cur.fetchone()
    print output
except:
    print "unable to print output"
    

# End Test Code Block
##############################
"""

##############################
# Test Code Block
# create player with UID

# End Test Code Block
##############################
