# -*- coding: utf-8 -*-

from PIL                            import Image, ImageDraw
from minecrafttools.intcoordinates  import IntCoordinates

import itertools
import os
import sys

class Map:

    def __init__(self, name, dimension, coordinates, colorsMap, lastModification, mapDimensions):
        """ Creates a Map object
        Params:
            name (string):                     the Map name (ex: map_8)
            dimension (integer):               dimension (nether = -1, surface = 0, end = ?)
            coordinates (IntCoordinates):      top left coordinates
            colorsMap (ColorsMap):             list of colors ID and their references
            lastModification (integer):        last modification timestamp
            mapDimensions (MapDimensions):     map size informations
        """
        self.__name             = name
        self.__dimension        = int(dimension)
        self.__coordinates      = coordinates
        self.__colorsMap        = colorsMap
        self.__lastModification = lastModification
        self.__mapDimensions    = mapDimensions

    def heightInPixels(self):
        """ Returns the map height, in pixels
        Returns:
            integer
        """
        return self.__mapDimensions.height() * pow(2, self.__mapDimensions.scale())

    def lastModification(self):
        """ Returns the last modification timestamp
        Returns:
            integer
        """
        return self.__lastModification

    def left(self):
        """ Returns the map left coordinate, in pixels
        Returns:
            integer
        """
        return int(self.__coordinates.intValues()[0] - (self.widthInPixels() / 2))

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
        scale       = self.__mapDimensions.scale() + 1
        pictureSize = (self.__mapDimensions.width() * scale, self.__mapDimensions.height() * scale)
        picture     = Image.new('RGB', pictureSize, self.__colorsMap.rgbDefaultColor())
        draw        = ImageDraw.Draw(picture)

        for height in range(self.__mapDimensions.height()):
            for width in range(self.__mapDimensions.width()):
                x       = width * scale
                y       = height * scale
                color   = self.__colorsMap.rgbColor(IntCoordinates(width, height))

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
        pass # TODO MLG: saveFragments()

    def saveInto(self, draw, xOffset = 0, yOffset = 0):
        """ Saves the Map into an existing picture
        Params:
            draw    (Draw):     The ImageDraw.Draw where to save the Map
            xOffset (integer):  Starting horizontal position
            yOffset (integer):  Starting vertical position
        Returns:
            Map
        """
        scale = pow(2, self.__mapDimensions.scale())

        for height in range(self.__mapDimensions.height()):
            for width in range(self.__mapDimensions.width()):
                x = width * scale + xOffset
                y = height * scale + yOffset

                # do not draw the default color
                if self.__colorsMap.isDefaultColor(IntCoordinates(width, height)):
                    continue

                draw.rectangle(
                    [x, y, x + scale - 1, y + scale - 1],
                    fill = self.__colorsMap.rgbColor(IntCoordinates(width, height))
                )

        return self

    def scale(self):
        """ Returns the map scale
        Returns:
            integer
        """
        return self.__mapDimensions.scale()

    def top(self):
        """ Returns the map top coordinate, in pixels
        Returns:
            integer
        """
        return int(self.__coordinates.intValues()[1] - (self.heightInPixels() / 2))

    def widthInPixels(self):
        """ Returns the map width, in pixels
        Returns:
            integer
        """
        return self.__mapDimensions.width() * pow(2, self.__mapDimensions.scale())
