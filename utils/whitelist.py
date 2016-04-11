# -*- coding: utf-8 -*-

from utils.player import Player

import json
import operator
import sys

class Whitelist:

    """ TODO class definition """

    def __init__(self, whitelistPath):
        self.__players          = {}
        self.__whitelistPath    = whitelistPath

        try:
            with open(whitelistPath) as whitelistFile:
                whitelist = json.load(whitelistFile)
        except IOError as error:
            print('Erreur lors de l\'accès à la whitelist : ' + error.errno)
            sys.exit(2)

        for entry in whitelist:
            self.addPlayer(
                Player(entry['uuid'], entry['name'])
            )

    def addPlayer(self, player):
        """ Add a player to the whitelist

        Args:
            player (Player): The player to add

        Returns:
            Whitelist
        """
        self.__players[player.name()] = player
        return self

    def playersSortedByName(self):
        """ Sort the players in the whitelist by name """
        return sorted(self.__players, key = lambda player: player.name)

    def removePlayer(self, playerName):
        """ Remove a player from the whitelist

        Args:
            playerName (string): The name of the player to remove

        Returns:
            Whitelist
        """
        del self.__players[playerName]
        return self

    def save(self):
        """ Save the whitelist

        Returns:
            Whitelist

        Raises:
            IOError: If the file cannot be written for any reason
        """
        pass
