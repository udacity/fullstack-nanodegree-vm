#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def executeAndCommit(query, data=()):
    """This function provide functionality to execute query on database
        and commit maded changes

    Args:
        query: query to execute in db with commiting changes
        data: data need to pass for execute method
    """
    c = connect()
    cur = c.cursor()
    # If there is no data to execute, than not pass it to execute method
    if not data:
        cur.execute(query)
    else:
        cur.execute(query, data)
    c.commit()
    c.close()


def executeAndFetch(query):
    """This function provide functionality to execute query on database
    and return all rows from it.

    Args:
        query: query to execute in db and fetch result
    Returns:
        all rows returned by query
    """
    c = connect()
    cur = c.cursor()
    cur.execute(query)
    data = cur.fetchall()
    c.close()
    return data


def deleteMatches():
    """Remove all the match records from the database."""
    executeAndCommit("DELETE FROM matches")


def deletePlayers():
    """Remove all the player records from the database."""
    executeAndCommit("DELETE FROM players")


def countPlayers():
    """Returns the number of players currently registered."""
    data = executeAndFetch("SELECT COUNT(*) FROM players")
    # Players count is stored in first column of first row
    count = data[0][0]
    return count


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    executeAndCommit("INSERT INTO players (name) VALUES (%s)", (name,))


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,
    or a player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    return executeAndFetch("SELECT * FROM players_standings;")


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    executeAndCommit("INSERT INTO matches (winner_id, loser_id)\
                        VALUES (%s, %s)",
                     (winner, loser,))


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
    # mod(pw1.position, 2) = 1 - grab only even position players
    # pw2.position = pw1.position + 1 - grab next player ordered by wins
    return executeAndFetch("SELECT pw1.id, pw1.name, pw2.id, pw2.name \
                    FROM players_wins pw1, players_wins pw2 \
                    WHERE \
                    mod(pw1.position, 2) = 1 \
                    AND pw2.position = pw1.position + 1;")
