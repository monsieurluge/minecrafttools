# -*- coding: utf-8 -*-

from minecrafttools.intdimensions         import IntDimensions
from minecrafttools.minecraftmappixelized import MinecraftMapPixelized

class CartographyDimensions:

    def __init__(self, maps):
        """ Creates a CartographyDimensions object
        Params:
            maps (Maps): a list of maps which composes the cartography
        """
        self.__cache = []
        self.__maps  = maps

    def __dimensions(self):
        """ Returns the cartography dimensions
        Returns:
            IntDimensions
        """
        if len(self.__cache) > 0:
            return self.__cache[0]

        bottom = -999999
        left   = 999999
        right  = -999999
        top    = 999999

        for mapFile in self.__maps.maps():
            mapPixelized = MinecraftMapPixelized(mapFile.content())
            mapLeft      = mapPixelized.coordinates().longitude()
            mapTop       = mapPixelized.coordinates().latitude()
            mapHeight    = mapPixelized.dimensions().height()
            mapWidth     = mapPixelized.dimensions().width()

            if bottom < mapTop + mapHeight:
                bottom = mapTop + mapHeight

            if left > mapLeft:
                left = mapLeft

            if right < mapLeft + mapWidth:
                right = mapLeft + mapWidth

            if top > mapTop:
                top = mapTop

        self.__cache.append(IntDimensions(right - left, bottom - top))

        return self.__cache[0]

    def height(self):
        """ Returns the height
        Returns:
            integer
        """
        return self.__dimensions().height()

    def width(self):
        """ Returns the width
        Returns:
            integer
        """
        return self.__dimensions().width()
