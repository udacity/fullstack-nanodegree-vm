#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("<error message>")


def deleteMatches():
    """Remove all the match records from the database."""

    db, c = connect()
    c.execute("TRUNCATE matchup;")                  #clear rows in matchup table
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""

    db, c = connect()
    c.execute("TRUNCATE players CASCADE;")          #clear rows in players table
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""

    db, c = connect()
    c.execute("SELECT count(*) FROM players;")      #counts # of rows in players
    result = c.fetchone()
    db.close()
    return int(result[0])                           #return count of players


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db, c = connect()
    c.execute("INSERT INTO players (player_name) VALUES (%s);", (name,))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
`
    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, c = connect()
    query = ("SELECT * FROM standings;")
    c.execute(query)
    rows = c.fetchall()
    db.close()
    return rows


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the` id number of the player who won
      loser:  the id number of the player who lost
    """
    db, c = connect()
    c.execute("INSERT INTO matchup (winner, loser) VALUES (%s, %s) ", (winner, loser,))
    db.commit()
    db.close()


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

    rows = playerStandings()    #select all players from standings in win order

    i = True
    pairings = []
    idx = 0
    for row in rows:           #tuple format is (id1, username1, id2, username2)
        if i is True:
            (id1, player_name_1, wins, matches) = row                              #user_1
            i = False
        else:
            (id2, player_name_2, wins, matches) = row                              #user_2
            i = True
            pairings.append((id1, player_name_1, id2, player_name_2))
            idx=idx+1

    return pairings
