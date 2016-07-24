# -*- coding: utf-8 -*-

from minecrafttools.intdimensions import IntDimensions

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

        height = 3000
        width  = 3000

        # left   = None
        # top    = None
        # width  = 0
        # height = 0
        #
        # for mapFile in self.__maps.maps():
        #     minecraftMap = mapFile.content()
        #
        #     # move the top coordinate
        #     if top is None:
        #         top  = minecraftMap.coordinates().latitude()
        #     elif top > minecraftMap.coordinates().latitude():
        #         height += top - minecraftMap.coordinates().latitude()
        #         top = minecraftMap.coordinates().latitude()
        #
        #     # move the left coordinate
        #     if left is None:
        #         left  = minecraftMap.coordinates().longitude()
        #     elif left > minecraftMap.coordinates().longitude():
        #         width += left - minecraftMap.coordinates().longitude()
        #         left = minecraftMap.coordinates().longitude()
        #
        #     # increase the vertical size
        #     if top + height < minecraftMap.coordinates().latitude() + minecraftMap.dimensions().height():
        #         height += (minecraftMap.coordinates().latitude() + minecraftMap.dimensions().height()) - (top + height)
        #
        #     # increase the horizontal size
        #     if left + width < minecraftMap.coordinates().longitude() + minecraftMap.dimensions().width():
        #         width += (minecraftMap.coordinates().longitude() + minecraftMap.dimensions().width()) - (left + width)

        self.__cache.append(IntDimensions(width, height))

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
