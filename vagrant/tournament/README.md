# Tournament Result
### Background
This project is an attempt to perform Swiss Pairings using Python along with a Database for storing results. Swiss Pairings is a form of tournament Where we end up with an aggregate winner. Each round is played by all players where the players closest in points are played against each other. The winner is the player highest in rankings which depends on number of wins, matches and opponent wins.

### Core Files
* tournament.py
* tournament_test.py
* tournament.sql
 

## Database Definitions
The database program du jour is PostgreSQL
Using the file ```tournament.sql``` We are creating:
A database: tournament
Two tables:
* Players
* Matches

And the following views:
* Standings
* TotalMatches
* OpponentMatchWins
* TotalDraws
* TotalLosses
* TotalWins


## Tourmanent Algorithm
The solutions for the algorthm can be found in ```tournament.py```.
These are some of the keys solutions:
* Each player is registered onto the tournament and assigned an ID
* A match is inserted with a winner and a loser
* A buy is a match where only a winner is provided
* No rematches are allowed
* Only one buy per player in tournament
* Draws are allowed in the tournament
* Standings are sorted by: wins, opponent wins, draws, matches, losses, and name
* Each pair is screened to avoid rematch
 

## Tournament Tests
Each algorithm step is tested.
