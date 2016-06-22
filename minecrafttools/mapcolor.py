# -*- coding: utf-8 -*-

class MapColor:

    def __init__(self, id, description, red, green, blue):
        self.__id          = id
        self.__description = description
        self.__red         = red
        self.__green       = green
        self.__blue        = blue

    def rgb(self):
        """ Returns the RGB values in a tuple
        Returns:
            tuple: (red, green, blue)
        """
        return (int(self.__red), int(self.__green), int(self.__blue))
