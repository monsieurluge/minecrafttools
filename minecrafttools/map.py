# -*- coding: utf-8 -*-

from PIL                           import Image, ImageDraw
from minecrafttools.intcoordinates import IntCoordinates

import itertools
import os
import sys

class Map:

    def __init__(self, name, dimension, coordinates, colorsMap, lastModification):
        """ Creates a Map object
        Params:
            name (string):                map name (ex: map_8)
            dimension (integer):          dimension (nether = -1, surface = 0, end = ?)
            coordinates (IntCoordinates): top left coordinates
            colorsMap (ColorsMap):        list of colors ID and the dimensions of the map
            lastModification (integer):   last modification timestamp
        """
        self.__name             = name
        self.__dimension        = int(dimension)
        self.__coordinates      = coordinates
        self.__colorsMap        = colorsMap
        self.__lastModification = lastModification

    def heightInPixels(self):
        """ Returns the map height, in pixels
        Returns:
            integer
        """
        return self.__colorsMap.height() * pow(2, self.__colorsMap.scale())

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
        return int(self.__coordinates.longitude() - (self.widthInPixels() / 2))

    def name(self):
        """ Returns the Map name
        Returns:
            string
        """
        return self.__name

    def save(self, directory, colorsReference):
        """ Saves the map to a picture file (.png)
        Params:
            directory (string):                directory where to save the file
            colorsReference (ColorsReference): reference between map color ID's and rgb colors
        Returns:
            Map
        Raises:
            IOError: If the file cannot be written for any reason
        """
        scale       = self.__colorsMap.scale() + 1
        pictureSize = (self.__colorsMap.width() * scale, self.__colorsMap.height() * scale)
        picture     = Image.new('RGB', pictureSize, colorsReference.rgbDefaultColor())
        draw        = ImageDraw.Draw(picture)

        for height in range(self.__colorsMap.height()):
            for width in range(self.__colorsMap.width()):
                x       = width * scale
                y       = height * scale
                color   = colorsReference.rgb(self.__colorsMap.id(Coordinates(width, height)))

                draw.rectangle([x, y, x + scale - 1, y + scale - 1], fill = color)

        picture.save(os.path.join(directory, self.__name + '.png'))

        return self

    def saveFragments(self, directory, colorsReference):
        """ Explodes the Map into 128px*128px pictures
        Params:
            directory (string):                the directory where to store the pictures
            colorsReference (ColorsReference): reference between map color ID's and rgb colors
        Returns:
            Map
        Raises:
            IOError: If the file cannot be written for any reason
        """
        raise Exception('Map.saveFragments() can\'t be used for now') # TODO MLG: saveFragments()

    def saveInto(self, draw, xOffset, yOffset, colorsReference):
        """ Saves the Map into an existing picture
        Params:
            draw    (Draw):                    the ImageDraw.Draw where to save the Map
            xOffset (integer):                 starting horizontal position
            yOffset (integer):                 starting vertical position
            colorsReference (ColorsReference): reference between map color ID's and rgb colors
        Returns:
            Map
        """
        scale = pow(2, self.__colorsMap.scale())

        for height in range(self.__colorsMap.height()):
            for width in range(self.__colorsMap.width()):
                x = width * scale + xOffset
                y = height * scale + yOffset

                # do not draw the default color
                if colorsReference.isDefaultColor(self.__colorsMap.id(Coordinates(width, height))):
                    continue

                draw.rectangle(
                    [x, y, x + scale - 1, y + scale - 1],
                    fill = colorsReference.rgb(self.__colorsMap.id(Coordinates(width, height)))
                )

        return self

    def scale(self):
        """ Returns the map scale
        Returns:
            integer
        """
        return self.__colorsMap.scale()

    def top(self):
        """ Returns the map top coordinate, in pixels
        Returns:
            integer
        """
        return int(self.__coordinates.latitude() - (self.heightInPixels() / 2))

    def widthInPixels(self):
        """ Returns the map width, in pixels
        Returns:
            integer
        """
        return self.__colorsMap.width() * pow(2, self.__colorsMap.scale())
