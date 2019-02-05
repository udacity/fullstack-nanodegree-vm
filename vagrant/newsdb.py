# "Database code" for the DB Forum.
import psycopg2
import bleach

def get_firstThree():
    """Return all posts from the 'database', most recent first."""
    conn = psycopg2.connect('dbname=news')
    cusor = conn.cursor()
    cusor.execute(
        "select method, status from log")
    result = cusor.fetchall()
    conn.close()
    return result

def get_popularauthors():
    """Return all posts from the 'database', most recent first."""
    conn = psycopg2.connect('dbname=news')
    cusor = conn.cursor()
    cusor.execute(
        "select name, sum from popularauthors")
    result = cusor.fetchall()
    conn.close()
    return result

def get_morethantwopercent():
    """Return all posts from the 'database', most recent first."""
    conn = psycopg2.connect('dbname=news')
    cusor = conn.cursor()
    cusor.execute(
        "select date, percenterror from morethantwopercent")
    result = cusor.fetchall()
    conn.close()
    return result