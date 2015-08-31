#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


"""Method to exit connection after commiting to  database"""
def exit(connection):
    connection.commit()
    connection.close()


def deleteMatches():
    """Remove all the match records from the database."""
    connection = connect()
    context = connection.cursor()

    """Call database to delete all matches."""
    context.execute("DELETE FROM Matches;")
    exit(connection)


def deletePlayers():
    """Remove all the player records from the database."""
    connection = connect()
    context = connection.cursor()

    """Call database to delete all registered players."""
    context.execute("DELETE FROM Players;")
    exit(connection)


def countPlayers():
    """Returns the number of players currently registered."""
    connection = connect()
    context = connection.cursor()

    """Call database to the Players' count."""
    context.execute("SELECT COUNT(*) FROM Players;")
    count = context.fetchone()
	
    connection.close()
    return count[0]


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    connection = connect()
    context = connection.cursor()

    """Call database to insert new player to tournament."""
    context.execute("INSERT INTO Players (name)  VALUES (%s);", (bleach.clean(name),))
    exit(connection)


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
    connection = connect()
    context = connection.cursor()
    
    """Call database to delete all matches."""
    context.execute("SELECT * FROM Standings;")
    result = context.fetchall()
    connection.close()
    
    return result


def reportMatch(winner, loser=None, is_a_draw=False):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost, Default value is 'None' which indicates a bye for the winner
	  is_a_draw: optional parameter that indicates whether the match is a draw. Default is false
    """
    connection = connect()
    context = connection.cursor()
    
    """If it is a bye insert the winner, otherwise insert all fields"""
    if loser==None:
        context.execute("""
        INSERT INTO Matches (winner_id) 
        SELECT %s 
        WHERE 
        NOT EXISTS (
        SELECT * FROM Matches 
        WHERE (winner_id=%s AND loser_id=0));""",(winner, winner,))
    else:
        context.execute("""
        INSERT INTO Matches (winner_id, loser_id, draw) 
        SELECT %s, %s, %s 
        WHERE 
        NOT EXISTS ( 
        SELECT * FROM Matches 
        WHERE (winner_id=%s AND loser_id=%s)
        OR (loser_id=%s AND winner_id=%s));""",(winner, loser, is_a_draw, winner, loser, winner, loser,))
    
    exit(connection)

 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
    
    If the number of registered players is odd, the last player in standings is ignored.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    """Access current standings"""
    standings = playerStandings()
    pairings = []
    buy_play=()
    last_index = len(standings) - 1
    iterations = []

    if len(standings)%2!=0:
        buy_play=selectBuyPlay(standings)
        standings.remove(buy_play)
  
    for iterate in range(0, len(standings)/2):
        iterations.append(iterate * 2)
 
    """Resetting the pairing to ensure no reruns"""
    standing = selectBestMatch(standings)

    """Creating the final pairs"""
    for player_index in iterations:
        pairing = ()
        for index in range(player_index, player_index + 2):
            pairing+=(standings[index][0],standings[index][1])
        pairings.append(pairing)

    """In case number of players are odd, the pairing has one singleton"""
    if buy_play!=():
        pairings.append((buy_play[0], buy_play[1]))

    """if last_index%2==0:
        pairings.append((standings[last_index][0],standings[last_index][1]))
    """
    return pairings


"""The draw count for the player given id."""
def playerDrawCount(id):
    """Returns the number of draw outcomes by a player."""
    connection = connect()
    context = connection.cursor()

    """Call database to the Players' draw count."""
    context.execute("SELECT draws FROM TotalDraws WHERE TotalDraws.id=%s;",[id])
    draws = context.fetchone()

    connection.close()
    return draws[0]

"""Select a player for buy"""
def selectBuyPlay(players):
    connection = connect()
    context = connection.cursor()

    result=()
    for player in players:
        context.execute("""SELECT winner_id FROM Matches WHERE winner_id=%s AND loser_id=0;""",[player[0]])
        res=context.fetchone()
        if res!=player[0]:
            result = player
            break

    connection.close
    return result


"""Select a player that has not matched before"""
def selectBestMatch(standings):
    connection = connect()
    context = connection.cursor()

    iterations=[]
    for iterate in range(0, len(standings)/2):
        iterations.append(iterate * 2)

    size = len(standings)
    for i in iterations:
        for j in range(i+1,size):
            context.execute("""
                SELECT winner_id FROM Matches WHERE winner_id=%s AND loser_id=%s
                UNION 
                SELECT loser_id FROM Matches WHERE winner_id=%s AND loser_id=%s;""",(standings[i][0],standings[j][0],standings[j][0],standings[i][0],))
            res=context.fetchall()
            if res==[]:
                if j!=i+1:
                    tmp=standings[i+1]
                    standings[i+1]=standings[j]
                    standings[j]=tmp
                break

    return standings
