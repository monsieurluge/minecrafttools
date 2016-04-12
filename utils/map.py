# -*- coding: utf-8 -*-

from utils.colorsreference import ColorsReference
from PIL                   import Image, ImageDraw

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
        scale   = self.__scale + 1
        picture = Image.new('RGB', (self.__width * scale, self.__height * scale), self.__colorsReference.idToRgb('default'))
        draw    = ImageDraw.Draw(picture)

        for height in range(self.__height):
            for width in range(self.__width):
                x       = width * scale
                y       = height * scale
                xOffset = x + scale - 1
                yOffset = y + scale - 1
                colorId = self.__colors[self.__width * height + width]

                draw.rectangle([x, y, xOffset, yOffset], fill = self.__colorsReference.idToRgb(colorId))

        picture.save(os.path.join(directory, self.__name + '.png'))

        return self

    def scale(self):
        """ Return the map scale

        Returns:
            integer
        """
        return self.__scale
