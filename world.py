# coding: utf8

import glob
import os
import re
import struct

from nbt import nbt

# ------------------------------------------------------------------------------
# TODO : class definition
# ------------------------------------------------------------------------------
class World:

    def __init__(self, worldFolder):
        # Default properties
        self.folder     = worldFolder
        self.players    = None
        self.maps       = {}
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
            map = mapFile.get('data')
            scale = map.get('scale').value
            if scale in self.maps.keys():
                self.maps[scale].append(map)
            else:
                self.maps[scale] = [map]

    # --------------------------------------------------------------------------
    # TODO : method definition
    # --------------------------------------------------------------------------
    def generateCartography(self, cartographyName):
        self.loadMaps()
        # todo

    # --------------------------------------------------------------------------
    # TODO : method definition
    # --------------------------------------------------------------------------
    def getPlayers(self):
        if self.players != None:
            return self.players

        for fileName in glob.glob(os.path.join(self.folder, 'playerdata', '*.dat')):
            nbtFile = nbt.NBTFile(fileName, rb)
            print nbtFile.name
