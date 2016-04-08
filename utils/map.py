# -*- coding: utf-8 -*-

from colorsreference import ColorsReference

import itertools
import os
import png

class Map:

    """ TODO class definition """

    __colorsReference = None

    def __init__(self, name, scale, dimension, width, height, xCenter, zCenter, colors):
        self.__name       = name
        self.__scale      = int(scale)
        self.__dimension  = int(dimension)
        self.__width      = int(width)
        self.__height     = int(height)
        self.__xCenter    = xCenter
        self.__zCenter    = zCenter
        self.__colors     = colors

        if self.__colorsReference is None:
            self.__colorsReference = ColorsReference()

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
                id    = self.__colors[self.__width * height + width]
                color = self.__colorsReference.idToRgb(id)

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
