# -*- coding: utf-8 -*-

from player import Player

import json
import sys

# ------------------------------------------------------------------------------
# TODO : class definition
# ------------------------------------------------------------------------------
class Whitelist:

    # --------------------------------------------------------------------------
    # TODO : method definition
    # --------------------------------------------------------------------------
    def __init__(self, whitelistPath):
        self.players = []

        try:
            with open(whitelistPath) as whitelistFile:
                whitelist = json.load(whitelistFile)
        except IOError as error:
            print 'Erreur lors de l\'accès à la whitelist : ' + error.errno
            sys.exit(2)

        for entry in whitelist:
            self.addPlayer(
                Player(entry['uuid'], entry['name'])
            )

    # --------------------------------------------------------------------------
    # TODO : method definition
    # --------------------------------------------------------------------------
    def addPlayer(self, player):
        self.players.append(player)

    # --------------------------------------------------------------------------
    # TODO : method definition
    # --------------------------------------------------------------------------
    def removePlayer(semf, playerName):
        pass
