#
# Database access functions for the web forum.
# 
import psycopg2
import psycopg2.extras
from datetime import datetime

## Database connection
#DB = psycopg2.connect("dbname=forum")

## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    DB = psycopg2.connect("dbname=forum")

    cursor = DB.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cursor.execute("select content, time from posts order by time desc")
    posts = cursor.fetchall() 

    DB.close()

    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    DB = psycopg2.connect("dbname=forum")

    cursor = DB.cursor()

    exstring = "insert into posts values (%s)", (content,)
    cursor.execute("insert into posts values (%s)", (content,))

    DB.commit()
    DB.close()

#DB.close()