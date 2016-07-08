# -*- coding: utf-8 -*-

from minecrafttools.cartographymultiple import CartographyMultiple
from minecrafttools.cartographyunique   import CartographyUnique
from minecrafttools.maps                import Maps

import os
import sys

class World:

    def __init__(self, folder):
        """ Creates a World object
        Params:
            folder (string): the folder where the Minecraft world is stored
        """
        # The world folder must exist
        if not os.path.exists(folder): # TODO MLG: remove this test from the constructor
            print('[ERROR] The world "' + folder + '" doesn\'t exists.')
            sys.exit(1)

        self.__folder  = folder
        self.__maps    = Maps(os.path.join(folder, 'data'))
        self.__players = {} # Players(os.path.join(worldFolder, 'data'))

    def cartography(self, cartographyType, outputFolder):
        """ Returns the cartography
        Parameters:
            cartographyType (string)
            outputFolder (string)
        Returns:
            Cartography
        Raises:
            ValueError: If the cartography type is not known
        """
        if cartographyType == 'multiple':
            return CartographyMultiple(self.__maps, outputFolder)
        elif cartographyType == 'unique':
            return CartographyUnique(self.__maps, outputFolder)

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
