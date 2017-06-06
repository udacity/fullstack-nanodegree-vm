import psycopg2
import random

def connect():
	return psycopg1.connect("dbname = tournament")
	
def deleteMatches():
	conn = connect()
	c = conn.cursor()
	c.execute("delete * from Matches;")
	conn.commit()
	conn.close()
	
def deletePlayers():
	conn = connect()
	c = conn.cursor()
	c.execute("delete * from Players;")
	conn.commit()
	conn.close()
	
def countPlayers():
	conn = connect()
	c = conn.cursor()
	
	c.execute("select count(*) from Players;")
	amount = c.fetchone()
	return int(amount)
	
	conn.close()
	
def registerPlayer(name):
	conn = connect()
	c = conn.cursor()
	
	c.execute("select nickname from Players;")
	
	if name in c:
	
		print "Nickname already occupied!"
		
	else:
	
		c.execute(
		"""INSERT into Players values
		(DEFAULT, %s, DEFAULT, 0, 0.00, DEFAULT);""", 
		(name)
		)
	
	
	conn.commit()
	conn.close()
	
def playerStandings():
	conn = connect()
	c = conn.cursor()
	
	c.execute(
	"""select id, nickname, wins, wins + loses as matches from Players
	order by wins desc;"""
	)
	return c.fetchall()
	
	conn.close()
	
def reportMatch(winner, loser):
	conn = connect()
	c = conn.cursor()
	
	# Winner stats update
	c.execute("update Players set wins = wins + 1 where id = %s;", (winner))
	c.execute("select wins, loses from Players where id = %s;", (winner))
	
	ratio = 0.00
	
	try:
		ratio = c[0] / c[1]
	except:
		ratio = 1.00
		
	c.execute("update Players set ratio = %s where id = %s;", (ratio, winner))
	
	
	# Loser stats update
	c.execute("update Players set loses = loses + 1 where id = %s;",(loser))
	c.execute("select wins, loses from Players where id = %s;", (loser))
	
	ratio = 0.00
	
	try:
		ratio = c[0] / c[1]
	except:
		ratio = 1.00
	
	c.execute("update Players set ratio = %s where id = %s;", (loser, ratio))

	
	# Matches table insert
	if winner or loser:
		draw = False
	else:
		draw = True
	
	c.execute(
	""" INSERT into Matches values 
	(DEFAULT, NULL, %s, %s, %s);""",
	(winner, loser, draw)
	)
	
	conn.commit()
	conn.close()

def swissPairings():
	conn = connect()
	c = conn.cursor()
	
	playersAmount = countPlayers()
	
	if playersAmount % 2 == 0:
	
		c.execute(
		"""
		select a.id, a.nickname, b.id, b.nickname 
		FROM Players a, Players b
		where a.wins = b.wins
		and a.id > b.id
		order by a.wins desc;
	
		"""
		)
	
		return c.fetchall()
		
	else:
	
		c.execute("select id from Players;")
		lottery = c.fetchall()
		lucky = random.choice(lottery)
		
		c.execute(
		"""
		select a.id, a.nickname, b.id, b.nickname 
		FROM Players a, Players b
		where a.wins = b.wins
		and a.id > b.id
		and (a.id or b.id != %s)
		order by a.wins desc;
	
		""",
		(lucky)
		)
	
		return c.fetchall()
	
	conn.close()







