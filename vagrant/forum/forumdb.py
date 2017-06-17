# "Database code" for the DB Forum.

import psycopg2, bleach

DBNAME = 'forum'

def get_posts():
  db = psycopg2.connect(database=DBNAME)
  cursor = db.cursor()
  cursor.execute('select content, time from posts order by time desc')
  result = cursor.fetchall()
  db.close()
  return result

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  db = psycopg2.connect(database=DBNAME)
  cursor = db.cursor()
  cursor.execute("insert into posts values (%s)", (bleach.clean(content),))
  db.commit()
  db.close()


