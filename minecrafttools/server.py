# -*- coding: utf-8 -*-

from minecrafttools.properties import Properties
from minecrafttools.whitelist  import Whitelist

import os

class Server:

    def __init__(self, minecraftDirectory):
        """ Creates a Server object
        Params:
            minecraftDirectory (string): the directory where to find the server.properties file
        """
        self.__minecraftDirectory = minecraftDirectory
        self.__properties         = Properties(os.path.join(minecraftDirectory, 'server.properties'))
        self.__whitelist          = Whitelist(os.path.join(minecraftDirectory, 'whitelist.json'))

    def printWhitelist(self):
        """ Displays the players list """
        for player in self.__whitelist.playersSortedByName():
            print(player.id + ' /// ' + player.name)

    def worldFolder(self):
        """ Returns the active world folder
        Returns:
            string
        """
        return os.path.join(self.__minecraftDirectory, self.__properties.valueOf('level-name'))
