# -*- coding: utf-8 -*-

import datetime
import glob
import nbt
import os
import re

from minecrafttools.colorsmap        import ColorsMap
from minecrafttools.intcoordinates   import IntCoordinates
from minecrafttools.intdimensions    import IntDimensions
from minecrafttools.minecraftmapfile import MinecraftMapFile

class Maps:
    # TODO MLG: makes this object a List

    def __init__(self, directory):
        """ Creates a Maps object
        Params:
            directory (string): the directory where are stored the maps
        """
        self.__directory  = directory
        self.__maps       = []
        self.__mapsLoaded = False

    def __loadMaps(self):
        """ Loads all the maps which were crafted in game """
        for path in glob.glob(os.path.join(self.__directory, '*.dat')):
            if not 'map_' in path:
                continue

            self.__maps.append(
                MinecraftMapFile(path)
            )

        self.__mapsLoaded = True # TODO MLG : ugly !

    def maps(self):
        """ Returns a list of maps """
        if self.__mapsLoaded is False:
            self.__loadMaps()

        return self.__maps
