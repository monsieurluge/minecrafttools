# -*- coding: utf-8 -*-

class MapColor:

    def __init__(self, id, description, red, green, blue):
        self.__id          = id
        self.__description = description
        self.__red         = int(red)
        self.__green       = int(green)
        self.__blue        = int(blue)

    def rgb(self):
        """ Returns the RGB values in a tuple

        Returns:
            tuple: (red, green, blue)
        """
        return (self.__red, self.__green, self.__blue)
