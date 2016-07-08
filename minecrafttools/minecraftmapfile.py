# -*- coding: utf-8 -*-

import nbt
import os
import re

from minecrafttools.colorsmap      import ColorsMap
from minecrafttools.intcoordinates import IntCoordinates
from minecrafttools.intdimensions  import IntDimensions
from minecrafttools.minecraftmap   import MinecraftMap
from nbt.nbt                       import NBTFile

class MinecraftMapFile:

    def __init__(self, path):
        """ Creates a MinecraftMapFile object
        Params:
            path (string): the path to the map file on disk
        """
        self.__path = path

    def content(self):
        """ Returns the content of the file
        Returns:
            MinecraftMap
        """
        nbtData = NBTFile(self.__path, 'rb').get('data')

        return MinecraftMap(
            self.name(),
            int(str(nbtData.get('dimension'))), # dimension (Nether, World, End, etc)
            IntCoordinates(
                str(nbtData.get('xCenter')),
                str(nbtData.get('zCenter'))
            ),
            ColorsMap(
                IntDimensions(
                    str(nbtData.get('width')),
                    str(nbtData.get('height'))
                ),
                int(str(nbtData.get('scale'))),
                nbtData.get('colors')
            ),
            self.lastModification()
        )

    def lastModification(self):
        """ Returns the file last modification time (timestamp)
        Returns:
            integer
        """
        return os.path.getmtime(self.__path)

    def name(self):
        """ Returns the map name (ex: map_12)
        Returns:
            string
        Raises:
            Exception if the file is not properly named
        """
        found = re.search('(map_\d+).dat', self.__path);

        if None == found:
            raise Exception('the file ' + path + ' is not a regular map file (wrong name)')

        return found.group(1)
