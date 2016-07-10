# -*- coding: utf-8 -*-

from minecrafttools.intcoordinates import IntCoordinates
from minecrafttools.intdimensions  import IntDimensions
from minecrafttools.minecraftmap   import MinecraftMap

class MinecraftMapPixelized:

    def __init__(self, minecraftMap):
        """ Creates a MinecraftMapPixelized object
        Params:
            minecraftMap (MinecraftMap): the map to "pixelize"
        """
        self.__origin = minecraftMap

    def coordinates(self):
        """ Returns the top left coordinates of the map
        Returns:
            IntCoordinates
        """
        return self.__origin.coordinates()

    def dimensions(self):
        """ Returns the dimensions of the map
        Returns:
            IntDimensions
        """
        return IntDimensions(
            self.__origin.dimensions().width() * pow(2, self.__origin.scale()),
            self.__origin.dimensions().height() * pow(2, self.__origin.scale())
        )

    def id(self, coordinates):
        """ Returns the color id at the given coordinates
        Params:
            coordinates (IntCoordinates): the coordinates of the color id
        Returns:
            integer
        Raises:
            IndexError when the coordinates are out of bound
        """
        return self.__origin.id(coordinates)

    def scale(self):
        """ Returns the map scale
        Returns:
            integer
        """
        return self.__origin.scale()

    def type(self):
        """ Returns the map type (surface, nether, end, etc)
        Returns:
            integer
        """
        # TODO MLG: return a string (or a map type object) instead of an integer
        return self.__origin.type()
