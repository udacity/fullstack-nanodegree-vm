#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach
from player import Player

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
    # IS THIS SORTED PROPERLY?
    c.execute(query)
    result = c.fetchall()
    DB.close()
    return result

def playerStanding(id):
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
    query = """SELECT r.Wins, r.Draws, r.Losses, r.Matches FROM players as p,
     registration as r WHERE r.PID = '%s' AND p.PID = r.PID""" % (id)
    c.execute(query)
    result = c.fetchall()
    DB.close()
    return result

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    winner_stats = playerStanding(winner)
    loser_stats = playerStanding(loser)
    winner_wins = winner_stats[0][0]
    winner_matches = winner_stats[0][3]
    winner_wins += 1
    winner_matches += 1
    loser_losses = loser_stats[0][2]
    loser_matches = loser_stats[0][3]
    loser_losses += 1
    loser_matches += 1
    DB = connect()
    c = DB.cursor()
    #TODO SQL does not match code or _test
    query = "INSERT INTO matches(Winner, Loser) VALUES ('%s', '%s')" % (winner, loser)
    c.execute(query)
    #WIN
    query = """UPDATE registration SET Wins='%d', Matches='%d'
    WHERE PID='%s'""" % (winner_wins, winner_matches, winner)
    c.execute(query)
    # LOSE
    query = """UPDATE registration SET Losses='%d', Matches='%d'
    WHERE PID='%s'""" % (loser_losses, loser_matches, loser)
    c.execute(query)
    DB.commit()
    DB.close()

def reportMatchDraw(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    winner_stats = playerStanding(winner)
    loser_stats = playerStanding(loser)
    winner_draws = winner_stats[0][1]
    winner_matches = winner_stats[0][3]
    winner_draws += 1
    winner_matches += 1
    loser_draws = loser_stats[0][1]
    loser_matches = loser_stats[0][3]
    loser_draws += 1
    loser_matches += 1
    DB = connect()
    c = DB.cursor()
    #GONNA NEED TO FIX THIS TOO
    query = "INSERT INTO matches(Winner, Loser, Draw) VALUES ('%s', '%s', 'TRUE')" % (winner, loser)
    c.execute(query)
    #WIN
    query = """UPDATE registration SET Draws='%d', Matches='%d'
    WHERE PID='%s'""" % (winner_draws, winner_matches, winner)
    c.execute(query)
    # LOSE
    query = """UPDATE registration SET Draws='%d', Matches='%d'
    WHERE PID='%s'""" % (loser_draws, loser_matches, loser)
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
    pid_list = []
    name_list = []
    record_list = []
    a = []
    # SELF JOIN?
    query = """SELECT p.PID, p.PName, r.Wins, r.Draws, R.Losses, r.Matches
    FROM players as p, registration as r WHERE p.PID = r.PID ORDER BY r.Wins"""
    c.execute(query)
    result = c.fetchall()
    for i, j in enumerate(result):
        pid_list.append(j[0])
        name_list.append(j[1])
        record = j[2] + j[3] / j[5]
        p = Player(j[0], j[1], j[2], j[3], j[4], j[5], record)
        a.append(p)
        record_list.append(record)
    #for i, j, k in zip(pid_list, name_list, record_list):
        #print i, j, k
    # DO SOMETHING WITH RESULTS TO SORT PAIRINGS, CREATE NEW TUPLE
    print a
    return result
    DB.close()
