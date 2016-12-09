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
    c.execute("TRUNCATE matchup;")                           #clear rows in matchup table
    c.execute("UPDATE players SET wins = 0, matches=0;")      #keeps rows in standings but resets matches and wins to 0
    db.commit()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""

    db, c = connect()
    c.execute("TRUNCATE players;")                           #clear rows in players table
    db.commit()
    db.close()

def countPlayers():
    """Returns the number of players currently registered."""

    db, c = connect()
    c.execute("SELECT count(*) FROM players;")                 #counts number of rows in players table
    result = c.fetchone()
    db.close()
    return int(result[0])                                      #return count of players

def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db, c = connect()
    c.execute("INSERT INTO players (username) VALUES (%s);", (name,))           #insert new player into platyers table
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
    c.execute("SELECT * FROM players ORDER BY wins;")
    rows = c.fetchall()                                                         #select all rows from standings and sort by wins
    db.close()                                                                  #return tuple with format (id, name, wins, matches)
    return rows

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the` id number of the player who won
      loser:  the id number of the player who lost
    """
    db, c = connect()
    c.execute("UPDATE players SET wins = wins+1, matches=matches+1 WHERE player_id=(%s);", (winner,)) #add a win to the winners standings and increment matches
    c.execute("UPDATE players SET matches=matches+1 WHERE player_id=(%s);", (loser,))                 #loser does not receive a win, increment matches
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

    rows = playerStandings()                                                      #select all players from standings in win order
    db, c = connect()

    i = True
    idx = 0
    pairings = []                                                               #select 2 rows at a time and create a pairing
    for row in rows:                                                            #tuple format is (id1, username1, id2, username2)
        if i == True:
            (id1, username_1, wins, matches) = row                              #user_1
            i = False
        else:
            (id2, username_2, wins, matches) = row                              #user_2
            i = True
            c.execute("INSERT INTO matchup VALUES (%s, %s, %s, %s);", (id1, username_1, id2, username_2,))
            idx = idx + 1                                                       #place this tuple row into matchup table

    c.execute("SELECT * FROM matchup")                                          #return all swiss pairing matchups
    rows = c.fetchall()
    db.close()
    return rows
