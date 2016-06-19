# -*- coding: utf-8 -*-

class ColorsMap:

    def __init__(self, dimensions, colors, colorsReference):
        self.__dimensions      = dimensions
        self.__colors          = colors
        self.__colorsReference = colorsReference

    def rgbDefaultColor(self):
        return self.__colorsReference.idToRgb('default')

    def isDefaultColor(self, intCoordinates):
        index = self.__dimensions.intValues()[1] * intCoordinates.intValues()[1] + intCoordinates.intValues()[0]

        if index > len(self.__colors):
            raise IndexError('these ColorsMap coordinates are out of bound : [' + str(intCoordinates.intValues()) + ']')

        return int(self.__colors[index]) == 0

    def rgbColor(self, intCoordinates):
        index = self.__dimensions.intValues()[1] * intCoordinates.intValues()[1] + intCoordinates.intValues()[0]

        if index > len(self.__colors):
            raise IndexError('these ColorsMap coordinates are out of bound : [' + str(intCoordinates.intValues()) + ']')

        return self.__colorsReference.idToRgb(self.__colors[index])
