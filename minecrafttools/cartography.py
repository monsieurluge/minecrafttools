# -*- coding: utf-8 -*-

from minecrafttools.colorsreference import ColorsReference

class Cartography:

    def __init__(self, maps):
        """ Creates a Cartography object
        Params:
            maps (Maps): a list of maps
        """
        self._colorsReference = ColorsReference()
        self._coordinates     = None # TODO MLG : find the right way to initialize the coordinates
        self._dimensions      = None # TODO MLG : find the right way to initialize the dimensions
        self._maps            = maps
