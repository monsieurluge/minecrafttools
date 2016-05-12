# -*- coding: utf-8 -*-

from nbt       import nbt
from utils.map import Map

import datetime
import glob
import os
import re

class Cartography:

    def __init__(self, mapsDirectory):
        self.__config           = None
        self.__directory        = mapsDirectory
        self._maps              = self.__loadMaps()
        self._top               = None
        self._left              = None
        self._horizontalSize    = 0
        self._verticalSize      = 0

    def __loadMaps(self):
        """ Loads all the maps (which were crafted in game)
        Returns:
            list
        """
        maps = []

        for mapFile in glob.glob(os.path.join(self.__directory, '*.dat')):
            if not 'map_' in mapFile:
                continue

            mapContent  = nbt.NBTFile(mapFile, 'rb')
            result      = re.search('(map_\d+).dat', mapFile);

            maps.append(Map(
                result.group(1),
                int(str(mapContent.get('data').get('scale'))),
                int(str(mapContent.get('data').get('dimension'))),
                int(str(mapContent.get('data').get('width'))),
                int(str(mapContent.get('data').get('height'))),
                int(str(mapContent.get('data').get('xCenter'))),
                int(str(mapContent.get('data').get('zCenter'))),
                mapContent.get('data').get('colors'),
                os.path.getmtime(mapFile)
            ))

        return maps
