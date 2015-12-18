#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

class Player:
    def __init__(self, id, name, wins, draws, losses, matches, record):
        self.id = id
        self.name = name
        self.wins = wins
        self.draws = draws
        self.losses = losses
        self.matches = matches
        self.record = record

    def __repr__(self):
        return repr((self.id, self.name, self.wins, self.draws,
                     self.matches, self.record))

    def match_record(self):
        return 0