# -*- coding: utf-8 -*-

from nbt       import nbt
from utils.map import Map

import glob
import os
import re

class Cartography:

    CARTOGRAPHY_FRAGMENTS = 'fragments'
    CARTOGRAPHY_MULTIPLE  = 'multiple'
    CARTOGRAPHY_UNIQUE    = 'unique'

    def __init__(self, mapsDirectory):
        self.__cartographyHorizontalSize    = 0
        self.__cartographyVerticalSize      = 0
        self.__cartographyWestCoordinates   = 0
        self.__cartographyNorthCoordinates  = 0
        self.__maps                         = []
        self.__directory                    = mapsDirectory

    def __generateFragments(self, outputDirectory):
        """ Generates a fragmented cartography (128px*128px pictures)

        Params:
            outputDirectory (string): The directory where to store the pictures
        """
        pass # TODO __generateFragments()

    def __generateMultiple(self, outputDirectory):
        """ Generates as many pictures as maps crafted in game

        Params:
            outputDirectory (string): The directory where to store the pictures
        """
        for map in sorted(self.__maps, key = lambda map: map.scale()):
            try:
                map.save(outputDirectory)
            except IOError as exception:
                print('[WARNING] Failure when trying to generate the "' + map.name() + '" map : ' + format(exception))

    def __generateUnique(self, outputDirectory):
        """ Generates an unique cartography picture

        Params:
            outputDirectory (string): The directory where to store the picture
        """
        pass # TODO __generateUnique()

    def __loadMaps(self):
        """ Loads all the maps (which were crafted in game) """
        for fileName in glob.glob(os.path.join(self.__directory, '*.dat')):
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

    def generate(self, outputDirectory, cartographyType):
        """ Generates the cartography picture file depending on the type

        Params:
            outputDirectory (string): The directory where create the picture
            cartographyType (string): The cartography output type

        Returns:
            World

        Raises:
            IOError: If the picture file cannot be created for any reason
        """
        if len(self.__maps) == 0:
            self.__loadMaps()

        if cartographyType == self.CARTOGRAPHY_FRAGMENTS:
            self.__generateFragments(outputDirectory)
        elif cartographyType == self.CARTOGRAPHY_MULTIPLE:
            self.__generateMultiple(outputDirectory)
        elif cartographyType == self.CARTOGRAPHY_UNIQUE:
            self.__generateUnique(outputDirectory)
        else:
            # TODO print a warning instead of generating a default cartography
            self.__generateMultiple(outputDirectory)

        print('[INFO] Cartography (' + cartographyType + ') successfully generated.')

        return self
