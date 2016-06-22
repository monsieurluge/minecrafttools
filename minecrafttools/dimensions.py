# -*- coding: utf-8 -*-

class Dimensions:

    def __init__(self, width, height):
        self.__width  = width
        self.__height = height

    def intValues(self):
        return tuple([
            int(self.__width),
            int(self.__height)
        ])
