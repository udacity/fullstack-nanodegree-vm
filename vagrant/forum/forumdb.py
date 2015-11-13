#
# Database access functions for the web forum.
#
import time
import psycopg2

## Database connection
conn = psycopg2.connect("dbname=forum")

## Open a cursor
cur = conn.cursor()

## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''

    #use a generator expression perhaps?
    allposts = []
    QUERY = cur.execute("SELECT content, time FROM posts ORDER BY time DESC;")
    print(QUERY)
    return allposts
    
## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    t = time.strftime('%c', time.localtime())
    cur.execute("INSERT INTO posts (time, content) VALUES (%s, %s);",
                (t, content))
