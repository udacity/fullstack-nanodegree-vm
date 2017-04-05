#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

class Player(object):
    def __init__(self, id, name, wins, draws, losses, matches):
        self.id = id
        self.name = name
        self.wins = wins
        self.draws = draws
        self.losses = losses
        self.matches = matches
        self.record = self.__match_record()

    def __repr__(self):
        return repr((self.id, self.name, self.wins, self.draws,
                     self.matches, self.record))

    def match_record(self):
        return (self.wins + self.draws) / float(self.matches)

    __match_record = match_record