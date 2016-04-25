#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#
import psycopg2
import psycopg2.extensions
from psycopg2.extensions import b
# we have to import the Psycopg2 extras library!
import psycopg2.extras
import sys
import collections
import itertools
from random import sample, choice, randrange
from operator import itemgetter, mul
from itertools import starmap, repeat, chain, cycle, tee, \
    groupby, count, combinations, starmap, islice
try:
    from itertools import imap as map, izip as zip, ifilter as filter, \
        izip_longest as zip_longest, ifilterfalse as filterfalse
except ImportError as err:
    from itertools import zip_longest, filterfalse



def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""

def main():
	#Define the connection string
	conn_string = 'host="localhost" dbname="tournament" user="postgres" password="secret"'
	# print the connection string to be used to connect
	print "Connecting to database\n	->%s" % (conn_string)
	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)
	# We refactor our connect() method
	# to deal not only with the database connection
	# but also with the cursor
	# since we can assign and return
	# multiple variables simultaneously.
	try:
		db = psycopg2.connect("dbname={}".format(database_name))
		cursor = db.cursor()
		return db, cursor
	except:
		print("Error when connecting the server")

	# By specifying a name for the cursor
	# psycopg2 creates a server-side cursor, which prevents all of the
	# records from being downloaded at once from the server.
	cursor = conn.cursor('cursor_unique_name', cursor_factory=psycopg2.extras.DictCursor)
	cursor.execute('SELECT * FROM table LIMIT 1000')
	# Because cursor objects are iterable we can just call 'for - in' on
	# the cursor object and the cursor will automatically advance itself
	# each iteration.
	# This loop should run 1000 times, assuming there are at least 1000
	# records in 'my_table'
	row_count = 0
	for row in cursor:
		row_count += 1
	print "row: %s    %s\n" % (row_count, row)
	# conn.cursor will return a cursor object; this cursor will
	# be used to perform queries
	print "Connected!\n"
 
if __name__ == "__main__":
	(main)
    

def deleteMatches():
    """Remove all the match records from the database."""
    db = psycopg2.connect("dbname=tournament")
    c = db.cursor()
    query = "TRUNCATE matches;"
    cursor.execute(query)
    db.commit()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    cursor = conn.cursor()
    query = "DELETE FROM players;"
    cursor.execute(query)
    conn.commit()
    conn.close()

def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    cursor = conn.cursor()
    query = "SELECT count(*) AS num FROM players;"
    cursor.execute(query)
    players_count = cur.fetchone()[0]
    conn.commit()
    conn.close()
    return count

def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player. (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
    name: the player's full name (need not be unique).
    """
    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO players (name) VALUES (%s);"
    parameter = (name,)
    cursor.execute = (query, parameter)
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
    conn = connect()
    cursor = conn.cursor()
    query = ("SELECT players.id, players.name, COUNT(matches.winner = players.id) AS wins, "
             "Count(matches.*) AS games"
             "FROM players LEFT JOIN matches "
             "ON players.id = matches.winner OR players.id = matches.loser,"
             "GROUP BY players.id, players.name "
             "ORDER BY wins DESC")
    # Because cursor objects are iterable we can just call 'for - in' on
    # the cursor object and the cursor will automatically advance itself
    # each iteration.
    # This loop should run as many times as there are
    # records in the table.
    parameter = (wins,)
    cursor.execute(query, parameter)
    row_count = 0
    for row in cursor:
        row_count += 1
        print "row: %s    %s\n" % (row_count, row)
    playerStandings = cur.fetchall() #Fetches all remaining rows of a query result, returning a list.
    conn.close()
    return playerStandings

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Args:
    winner: the id number of the player who won
    loser: the id number of the player who lost
    """
    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO matches (winner_id, loser_id) VALUES (%s, %s);"
    parameter = (winner, loser)
    cursor.execute(query, parameter)
    conn.commit()
    conn.close()

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
    db = psycopg2.connect("dbname=tournament")
    cursor = conn.cursor()
    query = ("SELECT players.id, players.name, COUNT(matches.winner = players.id) AS wins, FROM players LEFT JOIN matches, GROUP BY players.id, players.name ORDER BY Wins;")
    parameter = (id, name, matcheup, wins)
    cursor.execute(query, parameter)
    ids   = [ x[0] for x in c.fetchall () ] # unpack tuples
    names = [ x[0] for x in c.fetchall () ] # unpack tuples
    pairs = zip ([ x for x, in ids], [x for x, in names])
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
