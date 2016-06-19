# -*- coding: utf-8 -*-

import datetime
import glob
import nbt
import os
import re

from minecrafttools.colorsmap       import ColorsMap
from minecrafttools.colorsreference import ColorsReference
from minecrafttools.dimensions      import Dimensions
from minecrafttools.intcoordinates  import IntCoordinates
from minecrafttools.map             import Map
from minecrafttools.mapdimensions   import MapDimensions
from nbt.nbt                        import NBTFile

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

            nbtContent = NBTFile(mapFile, 'rb')
            nbtData    = nbtContent.get('data') # TODO MLG: convert properly bytes to int/string
            result     = re.search('(map_\d+).dat', mapFile);

            maps.append(
                Map(
                    result.group(1), # map file name (ex: map_12)
                    int(str(nbtData.get('dimension'))),
                    IntCoordinates(
                        str(nbtData.get('xCenter')),
                        str(nbtData.get('zCenter'))
                    ),
                    ColorsMap(
                        Dimensions(
                            str(nbtData.get('width')),
                            str(nbtData.get('height'))
                        ),
                        nbtData.get('colors'),
                        ColorsReference()
                    ),
                    os.path.getmtime(mapFile), # last modification
                    MapDimensions(
                        Dimensions(
                            str(nbtData.get('width')),
                            str(nbtData.get('height'))
                        ),
                        str(nbtData.get('scale'))
                    )
                )
            )

        return maps
