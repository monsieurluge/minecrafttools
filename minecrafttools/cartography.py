# -*- coding: utf-8 -*-

from minecrafttools.colorsreference import ColorsReference

class Cartography:

    def __init__(self, maps, folder):
        """ Creates a Cartography object
        Params:
            maps (Maps):     a list of maps
            folder (string): the folder where to store the cartography files
        """
        self._colorsReference = ColorsReference()
        self._coordinates     = None # TODO MLG : find the right way to initialize the coordinates
        self._dimensions      = None # TODO MLG : find the right way to initialize the dimensions
        self._folder          = folder
        self._maps            = maps
