#
# Database access functions for the web forum.
#
import time
import psycopg2

## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    DB = psycopg2.connect("dbname=forum")
    c = conn.cursor()
    c.execute("SELECT content, time FROM posts ORDER BY time DESC;")
    posts = [for row in c.fetchall()]

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    DB = psycopg2.connect("dbname=forum")
    c = conn.cursor()
    cur.execute("INSERT INTO posts (content) VALUES (%s,);",
                (content))
    DB.commit()
