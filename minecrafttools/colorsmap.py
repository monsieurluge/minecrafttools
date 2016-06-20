# -*- coding: utf-8 -*-

class ColorsMap:

    def __init__(self, dimensions, scale, colors):
        self.__dimensions      = dimensions
        self.__scale           = int(scale)
        self.__colors          = colors

    def id(self, coordinates):
        index = self.width() * coordinates.intValues()[1] + coordinates.intValues()[0]

        if index > len(self.__colors):
            raise IndexError('these ColorsMap coordinates are out of bound : [' + str(coordinates.intValues()) + ']')

        return int(self.__colors[index])

    def height(self):
        return self.__dimensions.intValues()[0]

    def scale(self):
        return self.__scale

    def width(self):
        return self.__dimensions.intValues()[1]
