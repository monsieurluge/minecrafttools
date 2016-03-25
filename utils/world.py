# -*- coding: utf-8 -*-

from nbt import nbt
from map import Map

import glob
import os
import re
import struct
import md5

# ------------------------------------------------------------------------------
# TODO : class definition
# ------------------------------------------------------------------------------
class World:

    def __init__(self, worldPath):
        # Default properties
        self.folder      = worldPath
        self.players     = None
        self.maps        = []

        # Cartography default properties
        self.cartographyHorizontalSize   = 0
        self.cartographyVerticalSize     = 0
        self.cartographyWestCoordinates  = 0
        self.cartographyNorthCoordinates = 0

        # The world folder must exist
        if not os.path.exists(self.folder):
            print 'Le monde "' + self.folder + '" n\'existe pas.'
            sys.exit(2)

        self.loadMaps()

    # --------------------------------------------------------------------------
    # TODO : method definition
    # --------------------------------------------------------------------------
    def loadMaps(self):
        for fileName in glob.glob(os.path.join(self.folder, 'data', '*.dat')):
            if not 'map_' in fileName:
                continue

            mapFile = nbt.NBTFile(fileName, 'rb')
            result  = re.search('(map_\d+).dat', fileName);

            map = Map(
                result.group(1),
                int(str(mapFile.get('data').get('scale'))),
                int(str(mapFile.get('data').get('dimension'))),
                int(str(mapFile.get('data').get('width'))),
                int(str(mapFile.get('data').get('height'))),
                int(str(mapFile.get('data').get('xCenter'))),
                int(str(mapFile.get('data').get('zCenter'))),
                mapFile.get('data').get('colors')
            )

            self.maps.append(map)

    # --------------------------------------------------------------------------
    # TODO : method definition
    # --------------------------------------------------------------------------
    def generateCartography(self, outputDirectory):
        # todo : load the colors ("Map colors.json")

        # sorted(self.players, key = lambda player: player.name)
        for map in sorted(self.maps, key = lambda map: map.scale):
            print '[' + str(map.scale) + '] ' + map.name
            # todo : create the picture

    # --------------------------------------------------------------------------
    # TODO : method definition
    # --------------------------------------------------------------------------
    def getPlayers(self):
        if self.players != None:
            return self.players

        for fileName in glob.glob(os.path.join(self.folder, 'playerdata', '*.dat')):
            nbtFile = nbt.NBTFile(fileName, rb)
            print nbtFile.name
