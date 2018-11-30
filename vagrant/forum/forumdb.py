# "Database code" for the DB Forum.
import psycopg2
import datetime
import bleach

#POSTS = [("This is the first post.", datetime.datetime.now())]

def get_posts():
  conn = psycopg2.connect("dbname=forum")
  cur = conn.cursor()
  query = "select content, time from posts order by time;"
  cur.execute(query)
  rows = cur.fetchall()

  """Return all posts from the 'database', most recent first."""
  return reversed(rows)

def add_post(content):
  conn = psycopg2.connect("dbname=forum")
  cur = conn.cursor()
  """Add a post to the 'database' with the current timestamp."""
  text = bleach.clean( str(content) )
  cur.execute("insert into posts values (%s)",(text,))
  conn.commit()
  conn.close()
  
