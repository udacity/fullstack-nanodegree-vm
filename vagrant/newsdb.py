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