#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def singleQuery(query, value):
    conn = connect()
    curr = conn.cursor()
    curr.execute(query, (value,))
    conn.commit()
    curr.close()
    conn.close()


def returnQuery(query, value):
    conn = connect()
    curr = conn.cursor()
    curr.execute(query, (value,))
    singleResult = curr.fetchone()[0]
    # conn.commit()
    curr.close()
    conn.close()
    return singleResult


def multiQuery(query, value, tournament):
    conn = connect()
    curr = conn.cursor()
    curr.execute(query, (value), (tournament,))
    multiResult = curr.fetchall()
    # conn.commit()
    curr.close()
    conn.close()
    return multiResult


def singleInsert(query, value, tournament):
    conn = connect()
    curr = conn.cursor()
    # testing code output
    # curr.mogrify("INSERT INTO players (player_name) VALUES (%s);", (name))
    print curr.mogrify(query, (value, tournament,),)
    curr.execute(query, (value, tournament,),)
    conn.commit()
    insert_id = curr.fetchone()[0]
    curr.close()
    conn.close()
    return insert_id


def iterativeQuery(query, value, tournament):
    conn = connect()
    curr = conn.cursor()
    listPairings = []
    curr.execute(query, (value,), (tournament,))
    while (curr.rownumber < curr.rowcount):
        pair = []
        for record in curr.fetchmany(2):
            pair += tuple(record)
        listPairings.append(tuple(pair))
        # for each pair of records make sure there is no match already in matches table - if no match, app to listPairings  # noqa
    return listPairings


def deleteMatches(tournament=1):
    query = "DELETE FROM matches WHERE tournament_id = %s;"
    singleQuery(query, tournament)


def deletePlayers(tournament=1):
    """Remove all the player records from the database."""
    # Delete the player records - cascades in place to ensure correct execution.
    query = "DELETE FROM players WHERE tournament_id = %s;"
    singleQuery(query, tournament)


def countPlayers(tournament=1):
    """Returns the number of players currently registered."""
    # Need to examine this code to see if it can be executed more efficiently.
    query = "SELECT count(1) from players WHERE tournament_id = %s;"
    return returnQuery(query, tournament)


def registerTournament(tournament=1):
    """Registers a new tournament
    If no tournaments exist, set a default tournament_id if none specified
    """
    query = """INSERT INTO tournament (tournament_name) VALUES (%s)
    RETURNING tournament_id"""
    return singleInsert(query, tournament)


def registerPlayer(name, tournament=1):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    # Insert the player name, no need to return anything
    query = "INSERT INTO players (player_name, tournament_id) VALUES (%s, %s);"
    return singleInsert(query, name, tournament)


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
    query = """SELECT * FROM playerStandings WHERE tournament_id = %s
    ORDER BY player_id ASC;"""
    return multiQuery(query, tournament)


def reportMatch(winner, loser, tournament = 1):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    query = "UPDATE matches SET played = played + 1 WHERE player_id IN %s AND tournament_id = %s;"  # noqa
    singleInsert(query, (winner, loser), (tournament),)
    query = "UPDATE matches SET score = score + 1 WHERE player_id IN (%s) AND tournament_id = %s;"
    singleInsert(query, (winner), (tournament),)


def swissPairings(tournament = 1):
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
    WHERE tournamentId = %s order by -score, -matches
    """
    return iterativeQuery(query, tournament)
