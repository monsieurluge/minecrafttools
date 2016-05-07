# -*- coding: utf-8 -*-

from utils.colorsreference import ColorsReference
from PIL                   import Image, ImageDraw

import itertools
import os
import sys

class Map:

    __colorsReference = None

    def __init__(self, name, scale, dimension, width, height, xCenter, zCenter, colors):
        """ Creates a Map object
        Params:
            name (string):          The Map name (ex: map_8)
            scale (integer):        scale of the Map
            dimension (integer):    dimension (nether = -1, surface = 0, end = ?)
            width (integer):        number of color id in the width (default: 128)
            height (integer):       number of color id in the height (default: 128)
            xCenter (integer):      x coordinate of the top left corner of the Map
            zCenter (integer):      z coordinate of the top left corner of the Map
            colors (list):          TODO
        """
        self.__name       = name
        self.__scale      = int(scale)
        self.__dimension  = int(dimension)
        self.__width      = int(width)
        self.__height     = int(height)
        self.__xCenter    = xCenter
        self.__zCenter    = zCenter
        self.__colors     = colors

        if self.__colorsReference is None:
            try:
                self.__colorsReference = ColorsReference()
            except IOError as exception:
                print('[ERROR] Failure when trying to load the colors reference: ' + format(exception))
                sys.exit(1)

    def name(self):
        """ Returns the Map name
        Returns:
            string
        """
        return self.__name

    def save(self, directory):
        """ Saves the map to a picture file (.png)
        Params:
            directory (string): directory where to save the file
        Returns:
            Map
        Raises:
            IOError: If the file cannot be written for any reason
        """
        scale       = self.__scale + 1
        pictureSize = (self.__width * scale, self.__height * scale)
        picture     = Image.new('RGB', pictureSize, self.__colorsReference.idToRgb('default'))
        draw        = ImageDraw.Draw(picture)

        for height in range(self.__height):
            for width in range(self.__width):
                x       = width * scale
                y       = height * scale
                colorId = self.__colors[self.__width * height + width]
                color   = self.__colorsReference.idToRgb(colorId)

                draw.rectangle([x, y, x + scale - 1, y + scale - 1], fill = color)

        picture.save(os.path.join(directory, self.__name + '.png'))

        return self

    def saveFragments(self, directory):
        """ Explodes the Map into 128px*128px pictures
        Params:
            directory (string): The directory where to store the pictures
        Returns:
            Map
        Raises:
            IOError: If the file cannot be written for any reason
        """
        pass # TODO saveFragments()

    def saveInto(self, picture, xOffset = 0, yOffset = 0):
        """ Saves the Map into an existing picture
        Params:
            picture (Image):    The picture where to draw the Map
            xOffset (integer):  Starting horizontal position
            yOffset (integer):  Starting vertical position
        Returns:
            Map
        Raises:
            IOError: If the file cannot be written for any reason
        """
        pass # TODO saveInto()

    def scale(self):
        """ Returns the map scale
        Returns:
            integer
        """
        return self.__scale
