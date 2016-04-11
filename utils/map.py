# -*- coding: utf-8 -*-

from utils.colorsreference import ColorsReference
from PIL                   import Image

import itertools
import os

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
        colorsList = self.__height * [None]
        for height in range(self.__height):
            colorsList[height] = (self.__width * 3) * [None]

            for width in range(self.__width):
                id    = self.__colors[self.__width * height + width]
                color = list(self.__colorsReference.idToRgb(id))

                colorsList[height][width] = color[0]
                colorsList[height][width + 1] = color[1]
                colorsList[height][width + 2] = color[2]
            colorsList[height] = tuple(colorsList[height])

        # pictureFile = open(os.path.join(directory, self.__name + '.png'), 'wb')
        # pngWriter   = png.Writer(self.__width, self.__height)
        #
        # pngWriter.write(pictureFile, colorsList)

        return self

    def scale(self):
        """ Return the map scale

        Returns:
            integer
        """
        return self.__scale
