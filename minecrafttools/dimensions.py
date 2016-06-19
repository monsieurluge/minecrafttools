# -*- coding: utf-8 -*-

class Dimensions:

    def __init__(self, width = 0, height = 0):
        self.__width  = width
        self.__height = height

    def intValues(self):
        return tuple([
            int(self.__width),
            int(self.__height)
        ])
