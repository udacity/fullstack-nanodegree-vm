# "Database code" for the DB Forum.
import psycopg2
import bleach


def get_popularauthors():
    """Return three popular authors of all time from the 'database', most recent first."""
    conn = psycopg2.connect('dbname=news')
    cusor = conn.cursor()
    cusor.execute(
        "select name, sum from popularauthors")
    result = cusor.fetchall()
    conn.close()
    return result

def get_morethantwopercent():
    """Return highest error from logged date from the 'database', most recent first."""
    conn = psycopg2.connect('dbname=news')
    cusor = conn.cursor()
    cusor.execute(
        "select date, percenterror from morethantwopercent")
    result = cusor.fetchall()
    conn.close()
    return result


def get_allpercenterror():
    """Return all error logs from the 'database', most recent first."""
    conn = psycopg2.connect('dbname=news')
    cusor = conn.cursor()
    cusor.execute(
        "select date, percenterror from allerrorpercentage")
    result = cusor.fetchall()
    conn.close()
    return result

def get_firstthree():
    """Return all articles from the 'database', most recent first."""
    conn = psycopg2.connect('dbname=news')
    cusor = conn.cursor()
    cusor.execute(
        "select title, num from articlelogdatas limit 3")
    result = cusor.fetchall()
    conn.close()
    return result