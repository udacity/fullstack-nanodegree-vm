#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import dbconnect
import psycopg2
###
# Note to self - make a generic connection class with inserts and
# returns as needed
###


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def singleQuery(**kwargs):
    conn = connect()
    curr = conn.cursor()
    query = kwargs.get('query')
    value = kwargs.get('value')
    name = kwargs.get('name')
    numResults = kwargs.get('numResults', 0)
    tournament = kwargs.get('tournament')
    if ('tournament' in kwargs and 'value' in kwargs):
        curr.execute(query, value, (tournament,))
    elif ('tournament' in kwargs and 'name' in kwargs):
        curr.execute(query, (name, tournament,))
    elif ('tournament' in kwargs and 'value' not in kwargs):
        curr.execute(query, (tournament,))
    else:
        curr.execute(query, (value,))
    if numResults == 1:
        Result = curr.fetchone()[0]
    elif numResults == "all":
        Result = curr.fetchall()
    else:
        conn.commit()
        curr.close()
        conn.close()
        return
    conn.commit()
    curr.close()
    conn.close()
    print Result
    return Result


def iterativeQuery(**kwargs):
    conn = connect()
    curr = conn.cursor()
    query = kwargs.get('query')
    # value = kwargs.get('value')
    # name = kwargs.get('name')
    # numResults = kwargs.get('numResults', 0)
    tournament = kwargs.get('tournament')
    listPairings = []
    # print curr.mogrify(query, (tournament,))
    curr.execute(query, (tournament,))
    while (curr.rownumber < curr.rowcount):
        pair = []
        for record in curr.fetchmany(2):
            pair += tuple(record)
        listPairings.append(tuple(pair))
        # for each pair of records make sure there is no match already in matches table - if no match, app to listPairings  # noqa
    return listPairings


def tidyDB():
    query = """
    TRUNCATE TABLE tournament CASCADE;"""
    singleQuery(query=query)

def deleteMatches(tournament=1):
    query = "DELETE FROM matches WHERE tournament_id = %s;"
    singleQuery(query=query, tournament=tournament)


def deletePlayers(tournament=1):
    """Remove all the player records from the database."""
    # Delete the player records - cascades in place to ensure correct execution.
    query = "DELETE FROM players WHERE tournament_id = %s;"
    singleQuery(query=query, tournament=tournament)


def countPlayers(tournament=1):
    """Returns the number of players currently registered."""
    # Need to examine this code to see if it can be executed more efficiently.
    query = "SELECT count(1) from players WHERE tournament_id = %s;"
    return singleQuery(query=query, tournament=tournament, numResults=1)


def registerTournament(name="Default"):
    """Registers a new tournament
    If no tournaments exist, set a default tournament_id if none specified
    """
    query = """INSERT INTO tournament (tournament_name) VALUES (%s)
    RETURNING tournament_id"""
    return singleQuery(query=query, name=name, numResults=1)


def registerPlayer(name, tournament=1):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    # Insert the player name, no need to return anything
    query = "INSERT INTO players (player_name, tournament_id) VALUES (%s, %s);"
    return singleQuery(query=query, name=name, tournament=tournament)


def playerStandings(tournament=1):
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
    # Return players and standings
    query = """SELECT player_id, player_name, score, played FROM
    playerStandings WHERE tournament_id = %s;"""
    return singleQuery(query=query, tournament=tournament, numResults="all")


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    query = "UPDATE matches SET played = played + 1 WHERE player_id IN %s;"  # noqa
    singleQuery(query=query, value=(winner, loser))
    query = "UPDATE matches SET score = score + 1 WHERE player_id IN (%s);"  # noqa
    singleQuery(query=query, value=(winner))


def swissPairings(tournament=1):
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
    query = """select player_id, player_name from playerStandings
    WHERE tournament_id = %s
    """
    return iterativeQuery(query=query, tournament=tournament)
