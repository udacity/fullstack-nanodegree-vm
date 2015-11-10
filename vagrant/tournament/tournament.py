#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


# Declare global variables here to be used across functions
psql = psycopg2
conn = psql.connect("dbname='tournament'")
cur = conn.cursor()
num = int


# Declare funtions to be used in applications of the database
def connect():
    """Connect to the PostgreSQL database.  Returns a database connection.
    check if database tournament exists
    else create
    """
    return psycopg2.connect("dbname='tournament'")


def deleteMatches():
    """Remove all the match records from the database.
    delete * from matches;
    """
    cur.execute("delete from matches where mID != 0")
    conn.commit()


def deletePlayers():
    """Remove all the player records from the database.
    delete * from players;
    """
    cur.execute("delete from players where PlayerID > 0")
    conn.commit()


def countPlayers():
    """Returns the number of players currently registered.
    select count(*) from players
    """
    cur.execute("""SELECT COUNT(*) FROM players""")
    output = cur.fetchone()
    return output[0]

def checkName(name):
    """
    This will eventually be able to check names to see if they have
    any special characters. Valid characters will include Letters
    both lowercase and capital, spaces for players who wish to have
    their first and last name listed, and apostrophies for players
    like "Boots O'Neal" who like to through things off.
    """
    # validate name for ' character
    if '\'' in name:
        name_part = name.split('\'')
        name = name_part[0]+'\'\''+name_part[1]
    return name


def registerPlayer(name):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    name = checkName(name)
    cur.execute("insert into players (name) values ('"+name+"')")
    conn.commit()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,
    or a player tied for first place if there is currently a tie.

    slect LastName, FirstName, Rank, Wins, matches order by rank desc

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    cur.execute("select PlayerID, name, Wins, Matches from players")
    output = cur.fetchall()
    return output


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost

      get current win count
      add new win
      display output
    """
    # add new match to all players after match
    matches = 0
    cur.execute("""select matches from players
                    where PlayerID = """ + str(winner) + """
                    or PlayerID = """ + str(loser))
    output = cur.fetchone()
    matches = int(output[0]) + 1
    cur.execute("update players set matches = " + str(matches) + """
                 where PlayerID = """ + str(winner) + """
                 or PlayerID = """ + str(loser))
    conn.commit()
    # get current wins of winners and add new wins
    cur.execute("select wins from players where PlayerID = "+str(winner))
    output = cur.fetchall()
    wins = output[0]
    cur_wins = int(wins[0]) + 1
    cur.execute("update players set wins = " + str(cur_wins) + """
                where PlayerID =""" + str(winner))
    conn.commit()
    cur.execute("select name, wins, matches from players")
    output = cur.fetchall()


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

        pull standings, limit to two results at a time
    """
    # check if number of players is even
    count = countPlayers()
    offset = 0
    match = ()
    if count % 2 == 0:
        # even number of players
        while offset < count:
            # get players from standings and create matches
            cur.execute("""select playerid, name from players
                            order by wins asc limit 2 offset """ + str(offset))
            offset += 1
            output = cur.fetchall()
            pair = [rows for rows in output]
            player1 = pair[0]
            player2 = pair[1]
            pid1 = str(player1[0])
            name1 = str(player1[1])
            name1 = checkName(name1)
            pid2 = str(player2[0])
            name2 = str(player2[1])
            name2 = checkName(name2)
            match = str(pid1 + ',\'' + name1 + '\',' + pid2 + ',\'' + name2 + '\'')
            cur.execute("""insert into matches (pid1, name1, pid2, name2)
                            values (""" + match + ")")
            cur.execute("select pid1, name1, pid2, name2 from matches")
            conn.commit()
            output = cur.fetchall()
            offset += 1
        return output

    else:
        count -= 1
        # odd number of players
        while offset < count:
            # get players from standings and create matches
            cur.execute("""select playerid, name from players
                            order by wins asc limit 2 offset """ + str(offset))
            offset += 1
            output = cur.fetchall()
            pair = [rows for rows in output]
            player1 = pair[0]
            player2 = pair[1]
            pid1 = str(player1[0])
            name1 = str(player1[1])
            name1 = checkName(name1)
            pid2 = str(player2[0])
            name2 = str(player2[1])
            name2 = checkName(name2)
            match = str(pid1 + ',\'' + name1 + '\',' + pid2 + ',\'' + name2 + '\'')
            cur.execute("""insert into matches (pid1, name1, pid2, name2)
                            values (""" + match + ")")
            cur.execute("select pid1, name1, pid2, name2 from matches")
            conn.commit()
            output = cur.fetchall()
            offset += 1
        return output

