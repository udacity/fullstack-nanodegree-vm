
from tournament import *

def testPreventRematches():
    standings = playerStandings()
    ids = [row[0] for row in standings]
    reportMatch(ids[0], ids[1])
    reportMatch(ids[2], ids[3])
    reportMatch(ids[4], ids[5])
    reportMatch(ids[6], ids[7])
    pairings = swissPairings()
    print(pairings)
    print()

deleteMatches()
deletePlayers()
players = ["Soundly Sorrows", "Fortunate Drapes", "Unbearable Cardboard", "Pinkie Pie",
               "Blue Bottle", "Some Attendee", "Ridiculous Artichoke", "Found Overhang"]
for player in players:
    registerPlayer(player)

for i in range(3):
    testPreventRematches()