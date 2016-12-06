#
# Database access functions for the web forum.
# 

import time

# import psycopg2 library
import psycopg2

# import bleach to clean spam :)
# https://bleach.readthedocs.org/en/latest/index.html
import bleach

## Database connection
#DB = []


## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''

    # connect to DB
    DB = psycopg2.connect('dbname=forum')

    # create cursor
    cur = DB.cursor()

    cur.execute("SELECT content, time, id FROM posts order by time")

    posts = cur.fetchall()
    
    # close connection
    DB.close()

    posts = [{'content': str(row[0]), 'time': str(row[1])} for row in posts]
    # print(posts)
    posts.sort(key=lambda row: row['time'], reverse=True)
    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''

    # clean content with bleach
    # bleach.clean(content)

    # connect to DB
    DB = psycopg2.connect('dbname=forum')

    t = time.strftime('%c', time.localtime())
    # DB.append((t, content))

    cur = DB.cursor()

    cur.execute("INSERT INTO posts (content, time) VALUES (%s, %s)", (content, t)) 
    # the parens and the tuple comm makes the forum safe agains the SQL injection attacks

    DB.commit()
 
    DB.close()




