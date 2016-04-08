# -*- coding: utf-8 -*-

class MapColor:

    # Blocks are colored according to their material.
    # Each material has a base color which is multiplied by 180, 220 or 255, and then divided by 255 to make the map color.
    # Each base color below is associated with four map colors - to get the first map color ID for a base color, multiply the base color ID by 4.

    def __init__(self, id, description, red, green, blue):
        self.__id          = id
        self.__description = description
        self.__red         = int(red)
        self.__green       = int(green)
        self.__blue        = int(blue)

    def rgb(self):
        """ Return the RGB values in a tuple

        Returns:
            tuple: (red, green, blue)
        """
        return (self.__red, self.__green, self.__blue)
