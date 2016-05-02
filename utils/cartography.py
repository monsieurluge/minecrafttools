# -*- coding: utf-8 -*-

from nbt       import nbt
from utils.map import Map

import datetime
import glob
import os
import re

class Cartography:

    CARTOGRAPHY_FRAGMENTS = 'fragments'
    CARTOGRAPHY_MULTIPLE  = 'multiple'
    CARTOGRAPHY_UNIQUE    = 'unique'

    def __init__(self, mapsDirectory):
        self.__config             = None
        self.__directory          = mapsDirectory
        self.__horizontalSize     = 0
        self.__maps               = None
        self.__topLeftCoordinates = [0, 0]
        self.__verticalSize       = 0

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
        """ Loads all the maps (which were crafted in game)

        Returns:
            Cartography
        """
        self.__maps = []

        for mapFile in glob.glob(os.path.join(self.__directory, '*.dat')):
            if not 'map_' in mapFile:
                continue

            lastModification = os.path.getmtime(mapFile)
            mapContent       = nbt.NBTFile(mapFile, 'rb')
            result           = re.search('(map_\d+).dat', mapFile);
            # TODO save the last modification date
            # print(result.group(1), datetime.datetime.fromtimestamp(lastModification))
            # TODO save the maps list in a file

            self.__maps.append(Map(
                result.group(1),
                int(str(mapContent.get('data').get('scale'))),
                int(str(mapContent.get('data').get('dimension'))),
                int(str(mapContent.get('data').get('width'))),
                int(str(mapContent.get('data').get('height'))),
                int(str(mapContent.get('data').get('xCenter'))),
                int(str(mapContent.get('data').get('zCenter'))),
                mapContent.get('data').get('colors')
            ))

        return self

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
