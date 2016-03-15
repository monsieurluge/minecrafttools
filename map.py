# coding: utf8

import os, nbt

class Map:

    def __init__(self, minecraftFolder):
        self.folder = os.path.join(minecraftFolder, 'playerdata')
        self.players = None

    # --------------------------------------------------------------------------
    # TODO : method definition
    # --------------------------------------------------------------------------
    def loadMaps(self):
        pass

    # --------------------------------------------------------------------------
    # TODO : method definition
    # --------------------------------------------------------------------------
    def getPlayers(self):
        if self.players != None:
            return self.players

        for fileName in glob.glob(os.path.join(self.folder, '*.dat')):
            nbtFile = nbt.NBTFile(fileName, rb)
            print nbtFile.name
