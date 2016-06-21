# -*- coding: utf-8 -*-

from minecrafttools.cartographymultiple import CartographyMultiple
from minecrafttools.cartographyunique   import CartographyUnique
from minecrafttools.maps                import Maps

import os
import sys

class World:

    def __init__(self, directory):
        """ Creates a World object
        Params:
            directory (string): the directory where the Minecraft world is stored
        """
        # The world folder must exist
        if not os.path.exists(directory): # TODO MLG: remove this test from the constructor
            print('[ERROR] The world "' + directory + '" doesn\'t exists.')
            sys.exit(1)

        self.__directory = directory
        self.__maps      = Maps(os.path.join(directory, 'data'))
        self.__players   = {} # Players(os.path.join(worldFolder, 'data'))

    def cartography(self, cartographyType):
        """ Returns the cartography
        Parameters:
            cartographyType (string)
        Returns:
            Cartography
        Raises:
            ValueError: If the cartography type is not known
        """
        if cartographyType == 'multiple':
            return CartographyMultiple(self.__maps)
        elif cartographyType == 'unique':
            return CartographyUnique(self.__maps)

        raise ValueError('"' + cartographyType + '" is not a valid cartography type')

    def players(self):
        """ Returns the players list
        Returns:
            dictionnary
        """
        return self.__players

        # for fileName in glob.glob(os.path.join(self.__folder, 'playerdata', '*.dat')):
        #     nbtFile = nbt.NBTFile(fileName, rb)
        #     print nbtFile.name
