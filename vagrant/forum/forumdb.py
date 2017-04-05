#
# Database access functions for the web forum.
# 

import psycopg2
import bleach

## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    try:
        DB = psycopg2.connect("dbname=forum")
        cur = DB.cursor()
        query = "SELECT time, content FROM posts ORDER BY time DESC"
        cur.execute(query)
        posts = ({'content': str(bleach.clean(row[1])), 'time': str(row[0])}
                 for row in cur.fetchall())
        DB.close()
    except:
        print "Cannot connect or retrieve..."

    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    try:
        DB = psycopg2.connect("dbname=forum")
        cur = DB.cursor()
        ## Cleanup:
        cleaned = bleach.clean(content, strip = True)
        ## Protect against SQL injection!:
        cur.execute("INSERT INTO posts (content) VALUES (%s)",
                    (cleaned,))
        DB.commit()
        DB.close()
    except psycopg2.DatabaseError, e:
        if DB:
            DB.rollback()
	print "Error '{0!s}'".format(e)
