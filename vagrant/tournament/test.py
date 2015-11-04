# create tournament date to input into database
# this will make it a lot easier to fill in tables 
# quickly to test funtions
from tournament import *
import psycopg2


players = 0
conn = psycopg2.connect("dbname='tournament'")
cur = conn.cursor()

def fillPlayers():
    pid = getID()
    cur.execute("insert into players (FirstName,LastName) values ('Bret','Wagner')")
    cur.execute("""insert into players (FirstName,LastName)
                values ('Player','Two')""")
    cur.execute("""insert into players (FirstName,LastName)
                values ('Brandon','Eller')""")
    cur.execute("""insert into players (FirstName,LastName)
                values ('Megan','Stratton')""")
    cur.execute("""insert into players (FirstName,LastName)
                values ('Real','Person')""")
    cur.execute("""insert into players (FirstName,LastName)
                values ('Awesome','Name')""")
    cur.execute("""insert into players (FirstName,LastName)
                values ('Less','Original')""")
    cur.execute("""insert into players (FirstName,LastName)
                values ('Another','Player')""")
    cur.execute("""insert into players (FirstName,LastName)
                values ('Eric','Dowell')""")
    cur.execute("""insert into players (FirstName,LastName)
                values ('Isaiah','Wagner')""")

fillPlayers()

conn.commit()

cur.execute("select * from players")
output = cur.fetchall()
for rows in output:
    print rows

conn.commit()
