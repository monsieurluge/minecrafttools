# -*- coding: utf-8 -*-

from minecrafttools.intcoordinates import IntCoordinates

class CartographyCoordinates:

    def __init__(self, maps):
        """ Creates a CartographyCoordinates object
        Params:
            maps (Maps): a list of maps which composes the cartography
        """
        self.__cache = []
        self.__maps  = maps

    def __coordinates(self):
        """ Returns the cartography coordinates
        Returns:
            IntCoordinates
        """
        if len(self.__cache) > 0:
            return self.__cache[0]

        left = 999999
        top  = 999999

        for mapFile in self.__maps.maps():
            minecraftMap = mapFile.content()

            if top > minecraftMap.coordinates().latitude():
                top = minecraftMap.coordinates().latitude()

            if left > minecraftMap.coordinates().longitude():
                left = minecraftMap.coordinates().longitude()

        self.__cache.append(IntCoordinates(left, top))

        return self.__cache[0]

    def latitude(self):
        """ Returns the latitude
        Returns:
            integer
        """
        return self.__coordinates().latitude()

    def longitude(self):
        """ Returns the longitude
        Returns:
            integer
        """
        return self.__coordinates().longitude()
