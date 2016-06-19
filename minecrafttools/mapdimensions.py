# -*- coding: utf-8 -*-

class MapDimensions:

    def __init__(self, dimensions, scale = 0):
        self.__dimensions = dimensions
        self.__scale      = scale

    def height(self):
        return int(self.__dimensions.intValues()[1])

    def scale(self):
        return int(self.__scale)

    def width(self):
        return int(self.__dimensions.intValues()[0])
