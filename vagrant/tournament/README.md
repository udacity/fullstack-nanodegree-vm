rdb-fullstack
=============

## How to start?

1. create the structure of the database(be sure you install the postgresql)
> $ psql -f tournament.sql
2.  test it(be sure you install python)
> $ python tournament_test.py
> 
> And you will see the result in the command line:
``` javascript

1. countPlayers() returns 0 after initial deletePlayers() execution.
2. countPlayers() returns 1 after one player is registered.
3. countPlayers() returns 2 after two players are registered.
4. countPlayers() returns zero after registered players are deleted.
5. Player records successfully deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After match deletion, player standings are properly reset.
9. Matches are properly deleted.
10. After one match, players with one win are properly paired.
Success!  All tests pass!
```
## just do it!