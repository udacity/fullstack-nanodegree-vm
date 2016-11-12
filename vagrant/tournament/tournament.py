#!/usr/bin/env python
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import logging

error_log = "error_log.txt"
# logging format
logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %('
                           'levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=error_log,
                    filemode='a')


def writeDb(sql, data):
    """
    write data to db
    """
    try:
        conn = connect()
        cursor = conn.cursor()
    except Exception, e:
        print e
        logging.error('db connect error:%s' % e)
        return False
    try:
        cursor.execute(sql, data)
        conn.commit()  # commit
    except Exception, e:
        conn.rollback()  # rollback
        logging.error('write data error:%s' % e)
        return False
    finally:
        cursor.close()
        conn.close()
    return True


def readDb(sql):
    """
        query
    """
    try:
        conn = connect()
        cursor = conn.cursor()
    except Exception, e:
        print e
        logging.error('db connect error:%s' % e)
        return False
    try:
        cursor.execute(sql)
        data = [dict(
            (cursor.description[i][0], value) for i, value in enumerate(row))
                for row in
                cursor.fetchall()]  # format
    except Exception, e:
        logging.error('query error:%s' % e)
        return False
    finally:
        cursor.close()
        conn.close()
    return data


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    conn = psycopg2.connect(database="tournament")
    return conn


def deleteMatches():
    """Remove all the match records from the database."""
    return writeDb("TRUNCATE TABLE t_match", None)


def deletePlayers():
    """Remove all the player records from the database."""
    return writeDb("TRUNCATE TABLE t_player CASCADE", None)


def countPlayers():
    """Returns the number of players currently registered."""
    data = readDb("SELECT COUNT(*) COUNT FROM t_player")
    return data[0]['count']


def registerPlayer(name):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    Args:
      name: the player's full name (need not be unique).
    """
    sql = "insert into t_player(player_name) VALUES(%s)"
    data = (name,)
    return writeDb(sql, data)


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place,
    or a player
    tied for first place if there is currently a tie.
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    # get all registered players
    data = readDb("select p_id,player_name from t_player")
    # construct the result
    result = list()
    for player in data:
        wins_num = readDb(
            "select count(*) count from t_match where won_p_id=" + str(
                int(player['p_id'])))[0]['count']
        lost_num = readDb(
            "select count(*) count from t_match where lost_p_id=" + str(
                int(player['p_id'])))[0]['count']
        standings = (player['p_id'], player['player_name'], int(wins_num),
                     int(wins_num + lost_num))
        result.append(standings)
    return result


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    sql = "insert into t_match(won_p_id,lost_p_id) VALUES(%s,%s)"
    data = (winner, loser,)
    return writeDb(sql, data)


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
    # check this whether is the first match
    pair_count = readDb("select count(*) count from t_match")[0]['count']
    # construct the result
    result = list()
    # first pair
    if int(pair_count) == 0:
        # get all registered players
        data = readDb("select p_id,player_name from t_player")
        for index in range(0, len(data) / 2, 1):
            standings = (
                data[index]['p_id'], data[index]['player_name'],
                data[index + 1]['p_id'],
                data[index + 1]['player_name'])
            result.append(standings)
    # not first pair
    else:
        # swissPair for win
        win_players_id = readDb("select won_p_id from t_match")
        appendPairs(result, win_players_id, "won_p_id")
        lost_players_id = readDb("select lost_p_id from t_match")
        appendPairs(result, lost_players_id, "lost_p_id")

    return result


def appendPairs(result, win_players_id, win_or_lost_key_words):
    p_ids_str = "("
    # construct the query
    for p_id in win_players_id:
        p_ids_str += str(p_id[win_or_lost_key_words]) + ","
    # cut the last ","
    p_ids_str = p_ids_str[0:len(p_ids_str) - 1]
    p_ids_str += ")"
    query = "select p_id,player_name from t_player where p_id in " + p_ids_str
    win_palyers_data = readDb(query)
    for index in range(0, len(win_palyers_data) / 2, 1):
        standings = (
            win_palyers_data[index]['p_id'],
            win_palyers_data[index]['player_name'],
            win_palyers_data[index + 1]['p_id'],
            win_palyers_data[index + 1]['player_name'])
        result.append(standings)
        # swissPair for lost
