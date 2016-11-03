#
# Database access functions for the web forum.
#
import psycopg2
import time
import bleach

# Get posts from database.


def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    DB = psycopg2.connect("dbname=forum")
    cursor = DB.cursor()
    query = "SELECT * FROM posts ORDER BY time DESC"
    cursor.execute(query)
    #posts = cursor.fetchall()
    posts = ({'content': str(row[1]), 'time': str(row[0])}
             for row in cursor.fetchall())
    # posts = [{'content': str(row[1]), 'time': str(row[0])}
    #        for row in c.fetchall

    DB.close()
    return posts

# Add a post to the database.


def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    #t = time.strftime('%c', time.localtime())
    DB = psycopg2.connect("dbname=forum")
    c = DB.cursor()
    q = "INSERT INTO posts (content) VALUES (%s)"
    d = (bleach.clean(content), )
    c.execute(q, d)
    DB.commit()
    DB.close()

    #DB.append((t, content))
