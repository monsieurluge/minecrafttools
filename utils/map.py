# -*- coding: utf-8 -*-

from mapColor import MapColor

import itertools
import json
import os
import png

class Map:

    """ TODO class definition """

    __mapColors = None

    def __init__(self, name, scale, dimension, width, height, xCenter, zCenter, colors):
        self.__name       = name
        self.__scale      = int(scale)
        self.__dimension  = int(dimension)
        self.__width      = int(width)
        self.__height     = int(height)
        self.__xCenter    = xCenter
        self.__zCenter    = zCenter
        self.__colors     = colors

        self.__loadMapColors()

    def __colorFromId(self, id):
        """ TODO method definition """
        baseId   = int(id / 4) * 4 + 2
        multiply = [180, 220, 255, 135]

        if not Map.__mapColors.has_key(baseId):
            return Map.__mapColors['default'].rgb()

        rgb = map(lambda color: color * multiply[id % 4] / 255, Map.__mapColors[baseId].rgb())

        return rgb

    def __loadMapColors(self):
        """ TODO method definition """
        if Map.__mapColors is not None:
            return

        data            = json.load(open(os.path.join(os.path.dirname(__file__), 'map colors.json')))
        Map.__mapColors = {}

        for element in data['colors']:
            Map.__mapColors[element['id']] = MapColor(
                element['id'],
                element['description'],
                element['red'],
                element['green'],
                element['blue']
            )

    def save(self, directory):
        """ Save the map to a picture file (.png)

        Params:
            directory (string): directory where to save the file

        Returns:
            Map

        Raises:
            IOError: If the file cannot be written for any reason
        """
        colorsList = []
        for height in range(self.__height):
            colorsList.append([])
            for width in range(self.__width):
                color = self.__colorFromId(self.__colors[self.__width * height + width])
                colorsList[height].append(color[0])
                colorsList[height].append(color[1])
                colorsList[height].append(color[2])
            colorsList[height] = tuple(colorsList[height])

        pictureFile = open(os.path.join(directory, self.__name + '.png'), 'wb')
        pngWriter   = png.Writer(self.__width, self.__height)

        pngWriter.write(pictureFile, colorsList)

        return self

    def scale(self):
        """ Return the map scale

        Returns:
            integer
        """
        return self.__scale
