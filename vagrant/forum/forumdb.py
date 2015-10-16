#
# Database access functions for the web forum.
#

import time

# Import PostgreSQL DB-API module
import psycopg2

## Database connection
DB = []

## Get posts from database.
def GetAllPosts():
    # connect the db
    # the db name is 'forum', the table name is 'posts'
    # Every time we want to access the db, we need to connect to it
    # this connection object is good until you close it
    pg = psycopg2.connect("dbname = forum")
    cursor = pg.cursor()
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    # old code, posts was a list of dictionaries, each dictionary
    # had the keys, 'content' and 'time'
    # posts = [{'content': str(row[1]), 'time': str(row[0])} for row in DB]
    # posts.sort(key=lambda row: row['time'], reverse=True)

    cursor.execute("SELECT * FROM posts ORDER BY time DESC;")
    results = cursor.fetchall()
    # using a dictionary comprehension

    # since we are using parentheses, this will actually return a generator
    # object
    posts = ({'content': str(row[1]), 'time': str(row[0])} for row in results)

    # whereas if we use the brackets for a list like this
    # posts = [{'content': str(row[1]), 'time': str(row[0])} for row in results]

    #then we will get a list of dictionaries

    pg.close();
    return posts

## Add a post to the database.
def AddPost(content):
    # connect the db
    # the db name is 'forum', the table name is 'posts'
    pg = psycopg2.connect("dbname = forum")
    cursor = pg.cursor()
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''

    # need the extra comma after content because something about a tuple
    cursor.execute("INSERT INTO posts(content) VALUES('%s');" % content)

    # commit on the connection, not the cursor
    pg.commit()

    pg.close();
    #t = time.strftime('%c', time.localtime())
    #DB.append((t, content))
