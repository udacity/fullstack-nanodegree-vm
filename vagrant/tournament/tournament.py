#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def commit_query(*query):
    """
    Opens a connection, executes the given query, commits the query,
    then closes the connection.

    Args:
        query (str or tuple): a valid SQL query

    Example:
        commit_query("DELETE FROM players")
    """
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(*query)
    connection.commit()
    connection.close()


def fetch_query(*query):
    """
    Opens a connection, executes the given query, fetchs the result,
    closes the connection, and returns the result.

    Args:
        query (str or tuple): a valid SQL query

    Example:
        fetch_query("SELECT id from Players")
        ---> [query result]
    """
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(*query)
    result = cursor.fetchall()
    connection.close()
    return result


def deleteMatches():
    """Remove all the match records from the database."""
    commit_query("UPDATE players set wins = 0, losses = 0")


def deletePlayers():
    """Remove all the player records from the database."""
    commit_query("DELETE from Players")


def countPlayers():
    """Returns the number of players currently registered."""
    count = fetch_query("SELECT id from Players")
    return len(count)


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    commit_query("INSERT INTO players (name) values (%s)", (name,))


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    players = fetch_query(
        "SELECT p.id, p.name, p.wins, temp.matches "
        "FROM ("
        "    SELECT id, SUM(wins + losses) as matches "
        "    FROM players "
        "    GROUP BY id"
        "    ) temp JOIN players p ON p.id = temp.id "
        "ORDER BY wins desc")
    return players


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    commit_query(
        "UPDATE players SET wins = wins + 1 WHERE id = %s", (winner,))
    commit_query(
        "UPDATE players SET losses = losses + 1 WHERE id = %s", (loser,))


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
    players = playerStandings()
    pairings = []
    count = 0
    while count < len(players):
        pairings.append((players[count][0],
                        players[count][1],
                        players[count + 1][0],
                        players[count + 1][1]))
        count += 2
    return pairings
