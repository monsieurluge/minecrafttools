# coding: utf8

from nbt import nbt

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
        self.maps        = {}
        # Cartography default properties
        self.cartographyHorizontalSize   = 0
        self.cartographyVerticalSize     = 0
        self.cartographyWestCoordinates  = 0
        self.cartographyNorthCoordinates = 0
        # The world folder must exist
        if not os.path.exists(self.folder):
            print 'Le monde "' + self.folder + '" n\'existe pas.'
            sys.exit(2)

    # --------------------------------------------------------------------------
    # TODO : method definition
    # --------------------------------------------------------------------------
    def loadMaps(self):
        for fileName in glob.glob(os.path.join(self.folder, 'data', '*.dat')):
            if not 'map_' in fileName:
                continue

            mapFile = nbt.NBTFile(fileName, 'rb')
            map     = mapFile.get('data')
            scale   = map.get('scale').value

            # md = md5.new()
            # md.update('{:d}'.format(map['colors'][0]))
            # print md.digest()

            # todo :

            if scale in self.maps.keys():
                self.maps[scale].append(map)
            else:
                self.maps[scale] = [map]

    # --------------------------------------------------------------------------
    # TODO : method definition
    # --------------------------------------------------------------------------
    def generateCartography(self, outputDirectory):
        self.loadMaps()

        # todo : load the colors ("Map colors.json")

        for scale in reversed(self.maps.keys()):
            for map in self.maps[scale]:
                pass
                # todo : create the picture
                # print map['colors']

    # --------------------------------------------------------------------------
    # TODO : method definition
    # --------------------------------------------------------------------------
    def getPlayers(self):
        if self.players != None:
            return self.players

        for fileName in glob.glob(os.path.join(self.folder, 'playerdata', '*.dat')):
            nbtFile = nbt.NBTFile(fileName, rb)
            print nbtFile.name
