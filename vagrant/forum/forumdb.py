#
# Database access functions for the web forum.
# 
import psycopg2
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

    cursor = DB.cursor()

    cursor.execute("select content, time from posts order by time desc")
    #posts = cursor.fetchall() 

    print cursor.fetchall()

    posts = [{'content': str(row[1]), 'time': str(row[0])} for row in cursor.fetchall()]
    #posts.sort(key=lambda row: row['time'], reverse=True)

    print posts

    DB.close()

    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    #t = time.strftime('%c', time.localtime())
    #DB.append((t, content))

    DB = psycopg2.connect("dbname=forum")

    ctime = datetime.now()
    cursor = DB.cursor()

    #exstring = "insert into posts values (\'%s\', %s)" % (content, ctime) 
    exstring = "insert into posts values (\'%s\')" % (content)
    cursor.execute(exstring)

    DB.commit()
    DB.close()

#DB.close()