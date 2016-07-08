# -*- coding: utf-8 -*-

import datetime
import glob
import nbt
import os
import re

from minecrafttools.colorsmap       import ColorsMap
from minecrafttools.intcoordinates  import IntCoordinates
from minecrafttools.dimensions      import Dimensions
from minecrafttools.map             import Map
from nbt.nbt                        import NBTFile

class Maps:

    def __init__(self, directory):
        """ Creates a Maps object
        Params:
            directory (string): the directory where are stored the maps
        """
        self.__directory  = directory
        self.__maps       = []
        self.__mapsLoaded = False

    def __loadMaps(self):
        """ Loads all the maps (which were crafted in game) """
        for mapFile in glob.glob(os.path.join(self.__directory, '*.dat')):
            if not 'map_' in mapFile:
                continue

            nbtData = NBTFile(mapFile, 'rb').get('data')
            result  = re.search('(map_\d+).dat', mapFile);

            self.__maps.append(
                Map(
                    result.group(1), # map file name (ex: map_12)
                    str(nbtData.get('dimension')),
                    IntCoordinates(
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
        self.__mapsLoaded = True # TODO MLG : ugly !

    def maps(self):
        """ Returns a list of maps """
        if self.__mapsLoaded is False:
            self.__loadMaps()

        return self.__maps
