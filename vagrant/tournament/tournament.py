#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach
###
# Note to self - make a generic connection class with inserts and
# returns as needed
###


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def singleQuery(**kwargs):
    """Generic query object - pass in arguments, and only use declared variables
    to allow us to query database objects, the name, value, number of results
    and the tournament.  This allows us to simplify what the various methods
    are doing and reduce the amount of code written
    Names are one of; player, tournament
    Value is the integer represenation of the player's ID
    Query is either an insert, update or a select.
    Tournament is the ID of the tournament.
    """
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
        curr.execute(query, (bleach.clean(name), tournament,))
    elif ('tournament' not in kwargs and 'name' in kwargs):
        curr.execute(query, (bleach.clean(name),))
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
    # print Result
    return Result


def iterativeQuery(**kwargs):
    """Iterative query to process the players for a given tournament and
     generate new pairings.   This will be enhanced in a later iteration to
    verify players haven't met before"""
    conn = connect()
    curr = conn.cursor()
    query = kwargs.get('query')
    tournament = kwargs.get('tournament')
    listPairings = []
    curr.execute(query, (tournament,))
    while (curr.rownumber < curr.rowcount):
        pair = []
        for record in curr.fetchmany(2):
            pair += tuple(record)
        listPairings.append(tuple(pair))
        # for each pair of records make sure there is no match already in matches table - if no match, app to listPairings  # noqa
    return listPairings


def deleteMatches():
    """Clean up old matches - to be followed by delete from players """
    query = "DELETE FROM matches;"
    singleQuery(query=query)


def deletePlayers():
    """Remove all the player records from the database."""
    # Delete the player records - cascades in place to ensure correct execution.
    query = "DELETE FROM players;"
    singleQuery(query=query)


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
    RETURNING tournament_id;"""
    return singleQuery(query=query, name=name, numResults=1)


def registerPlayer(name, tournament=1):

    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    # Insert the player name, if there is no tournament provided, try to use
    # the lowest numbered, if this fails, then generate a new tournament.
    query = "INSERT INTO players (player_name, tournament_id) VALUES (%s, %s);"
    try:
        singleQuery(query=query, name=name, tournament=tournament)
    except:
        temp_tournament = registerTournament()
        singleQuery(query=query, name=name, tournament=temp_tournament)


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
    query = "INSERT INTO played (winner, loser) VALUES %s"
    singleQuery(query=query, value=(winner, loser))


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
    # Testing alternative query to see if I can get better results.
    # query = """select player_id1, player_name1, player_id2, player_name2 from
    # pairings where tournament_id  = %s"""
    # players = singleQuery(query=query, tournament=tournament, numResults="all")  # noqa
    query = """select player_id, player_name from playerStandings where
     tournament_id = %s"""
    players = iterativeQuery(query=query, tournament=tournament)
    return players
