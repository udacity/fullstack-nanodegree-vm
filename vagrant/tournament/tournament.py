#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    c = connect()
    cur = c.cursor()
    cur.execute("DELETE FROM matches")
    c.commit()
    c.close()


def deletePlayers():
    """Remove all the player records from the database."""
    c = connect()
    cur = c.cursor()
    cur.execute("DELETE FROM players")
    c.commit()
    c.close()


def countPlayers():
    """Returns the number of players currently registered."""
    c = connect()
    cur = c.cursor()
    cur.execute("SELECT COUNT(*) FROM players")
    rows = cur.fetchall()
    c.close()
    return rows[0][0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    c = connect()
    cur = c.cursor()
    cur.execute("INSERT INTO players (name) VALUES (%s)", (name,))
    c.commit()
    c.close()


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
    c = connect()
    cur = c.cursor()
    cur.execute("SELECT * FROM players_standings;")
    rows = cur.fetchall()
    c.close()
    return rows


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    c = connect()
    cur = c.cursor()
    cur.execute("INSERT INTO matches (winner_id, loser_id) VALUES (%s, %s)",
                (winner, loser,))
    c.commit()
    c.close()


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
    c = connect()
    cur = c.cursor()
    cur.execute("SELECT pw1.id, pw1.name, pw2.id, pw2.name \
                    FROM players_wins pw1, players_wins pw2 \
                    WHERE \
                    pw2.wins = pw1.wins \
                    AND pw2.position = pw1.position + 1;")
    rows = cur.fetchall()
    c.close()
    return rows
