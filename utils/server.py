# -*- coding: utf-8 -*-

from utils.properties import Properties
from utils.whitelist  import Whitelist
from utils.world      import World

import os

class Server:

    """ TODO class definition """

    def __init__(self, minecraftDirectory):
        self.__properties = Properties(os.path.join(minecraftDirectory, 'server.properties'))
        self.__whitelist  = Whitelist(os.path.join(minecraftDirectory, 'whitelist.json'))
        self.__world      = World(os.path.join(minecraftDirectory, self.__properties.valueOf('level-name')))

    def printWhitelist(self):
        """ Display the players list """
        for player in self.__whitelist.playersSortedByName():
            print(player.id + ' /// ' + player.name)

    def world(self):
        """ Return the world

        Returns:
            World
        """
        return self.__world
