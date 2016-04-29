# -*- coding: utf-8 -*-

from utils.cartography import Cartography

import os
import sys

class World:

    def __init__(self, worldFolder):
        # The world folder must exist
        if not os.path.exists(worldFolder):
            print('[ERROR] The world "' + worldFolder + '" doesn\'t exists.')
            sys.exit(1)

        self.__folder      = worldFolder
        self.__players     = {}
        self.__cartography = Cartography(os.path.join(worldFolder, 'data'))

    def cartography(self):
        """ Returns the cartography

        Returns:
            Cartography
        """
        return self.__cartography

    def players(self):
        """ Returns the players list

        Returns:
            dictionnary
        """
        return self.__players

        # for fileName in glob.glob(os.path.join(self.__folder, 'playerdata', '*.dat')):
        #     nbtFile = nbt.NBTFile(fileName, rb)
        #     print nbtFile.name
