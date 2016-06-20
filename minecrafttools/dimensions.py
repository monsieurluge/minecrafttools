# -*- coding: utf-8 -*-

class Dimensions:

    def __init__(self, width, height):
        self.__width  = int(width)
        self.__height = int(height)

    def intValues(self):
        return tuple([
            int(self.__width),
            int(self.__height)
        ])
