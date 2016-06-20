# -*- coding: utf-8 -*-

import datetime
import glob
import nbt
import os
import re

from minecrafttools.colorsmap       import ColorsMap
from minecrafttools.colorsreference import ColorsReference
from minecrafttools.dimensions      import Dimensions
from minecrafttools.coordinates     import Coordinates
from minecrafttools.map             import Map
from minecrafttools.mapdimensions   import MapDimensions
from nbt.nbt                        import NBTFile

class Cartography:

    def __init__(self, mapsDirectory):
        self.__config           = None
        self.__directory        = mapsDirectory
        self._maps              = self.__loadMaps() # TODO MLG: don't load the maps in the constructor !
        self._coordinates       = None # TODO MLG : find a way to set properly these coordinates
        self._dimensions        = None # TODO MLG : find a way to set properly these dimensions

    def __loadMaps(self):
        """ Loads all the maps (which were crafted in game)
        Returns:
            list
        """
        maps = []

        for mapFile in glob.glob(os.path.join(self.__directory, '*.dat')):
            if not 'map_' in mapFile:
                continue

            nbtData = NBTFile(mapFile, 'rb').get('data')
            result  = re.search('(map_\d+).dat', mapFile);

            maps.append(
                Map(
                    result.group(1), # map file name (ex: map_12)
                    str(nbtData.get('dimension')),
                    Coordinates(
                        str(nbtData.get('xCenter')),
                        str(nbtData.get('zCenter'))
                    ),
                    ColorsMap(
                        Dimensions(
                            str(nbtData.get('width')),
                            str(nbtData.get('height'))
                        ),
                        str(nbtData.get('scale')),
                        nbtData.get('colors')
                    ),
                    os.path.getmtime(mapFile) # last modification
                )
            )

        return maps
