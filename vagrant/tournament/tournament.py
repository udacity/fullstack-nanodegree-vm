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
    create_tournament()

def deletePlayers():
    """Remove all the player records from the database."""
    query = '''UPDATE players SET deleted = true;'''
    count = run_query(query)

def countPlayers():
    """Returns the number of players currently registered."""
    query = '''SELECT count FROM player_count;'''
    count = run_query(query)
    return count[0][0]


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    tournament_id = get_tournament_id()
    query = '''INSERT INTO players (player_name, tournament_id) VALUES (%s, %s);'''
    run_query(query, (name, tournament_id))
    print(name + " registered.")



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
    query = '''SELECT * FROM standings;'''
    return run_query(query)


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    tournament_id = get_tournament_id()
    query = '''INSERT INTO matches (tournament_id, first_player_id, second_player_id, winner_id ) VALUES (%s, %s, %s, %s);'''
    run_query(query, (tournament_id, winner, loser, winner))
 
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
    standings = playerStandings()
    matches = []
    match = ()
    match_count = 1;
    last_player = ''
    for player in standings:
        last_player = player
        if match_count == 2:
            match = match + (player[0], player[1])
            matches.append(match)
            match_count = 1
        else:
            match = (player[0], player[1])
            match_count += 1
            
    # if we end with player this player gets a free win to the next round       
    '''if match_count == 1:
        reportMatch(standings[:-1][0], 0)'''

    return matches

        

def run_query(query, query_data = "()"):
    """Records the outcome of a single match between two players.

    Args:
      query:  the query to execute
      data_query:  any tuple params to make sure sql is escaped
    """
    conn = connect()
    c = conn.cursor()
    c.execute(query, query_data)
    return_data = ""

    if query.find("SELECT") < 0:
        conn.commit()
    else:
        return_data = c.fetchall()

    conn.close()
    return return_data

def get_tournament_id():
    """Records the outcome of a single match between two players.

    Return:
      The data from the excuted query
    """
    query = '''SELECT current_tournament_id FROM tournament;'''
    count = run_query(query)
    return count[0][0]


def create_tournament():
    """Creates a new tournament."""
    query = '''INSERT INTO tournaments (tournament_name) VALUES ('The Big thing!');'''
    count = run_query(query)

#Start off a tourment the first time the script is ran
create_tournament()
