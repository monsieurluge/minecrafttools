# -*- coding: utf-8 -*-

from nbt import nbt
from map import Map

import glob
import os
import re
import struct

class World:

    """ TODO class definition """

    def __init__(self, worldPath):
        # Default properties
        self.__folder   = worldPath
        self.__players  = {}
        self.__maps     = []

        # Cartography default properties
        self.__cartographyHorizontalSize    = 0
        self.__cartographyVerticalSize      = 0
        self.__cartographyWestCoordinates   = 0
        self.__cartographyNorthCoordinates  = 0

        # The world folder must exist
        if not os.path.exists(self.__folder):
            print 'Le monde "' + self.__folder + '" n\'existe pas.'
            sys.exit(2)

        self.__loadMaps()

    def __loadMaps(self):
        """ Load all the maps (which were crafted in game) """
        for fileName in glob.glob(os.path.join(self.__folder, 'data', '*.dat')):
            if not 'map_' in fileName:
                continue

            mapFile = nbt.NBTFile(fileName, 'rb')
            result  = re.search('(map_\d+).dat', fileName);

            self.__maps.append(Map(
                result.group(1),
                int(str(mapFile.get('data').get('scale'))),
                int(str(mapFile.get('data').get('dimension'))),
                int(str(mapFile.get('data').get('width'))),
                int(str(mapFile.get('data').get('height'))),
                int(str(mapFile.get('data').get('xCenter'))),
                int(str(mapFile.get('data').get('zCenter'))),
                mapFile.get('data').get('colors')
            ))
    def generateCartography(self, outputDirectory):
        """ Generate the cartography picture file

        Params:
            outputDirectory (string): The directory where create the picture

        Returns:
            World

        Raises:
            IOError: If the picture file cannot be created for any reason
        """

        for map in sorted(self.__maps, key = lambda map: map.scale()):
            map.save(outputDirectory)

    def players(self):
        """ Return the players list

        Returns:
            dictionnary
        """
        return self.__players

        # for fileName in glob.glob(os.path.join(self.__folder, 'playerdata', '*.dat')):
        #     nbtFile = nbt.NBTFile(fileName, rb)
        #     print nbtFile.name
