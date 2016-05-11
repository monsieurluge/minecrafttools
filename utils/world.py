# -*- coding: utf-8 -*-

from utils.cartographymultiple  import CartographyMultiple
from utils.cartographyunique    import CartographyUnique

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

    def cartography(self, cartographyType):
        """ Returns the cartography
        Parameters:
            cartographyType (string)
        Returns:
            Cartography
        Raises:
            ValueError: If the cartography type is not known
        """
        cartographyFolder = os.path.join(self.__folder, 'data')

        if cartographyType == 'multiple':
            return CartographyMultiple(cartographyFolder)
        elif cartographyType == 'unique':
            return CartographyUnique(cartographyFolder)

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
