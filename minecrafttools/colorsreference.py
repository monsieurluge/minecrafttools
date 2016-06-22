# -*- coding: utf-8 -*-

from minecrafttools.mapcolor import MapColor

import json
import os

class ColorsReference:

    def __init__(self):
        """ Creates a ColorsReference object """
        self.__colors = {}
        self.__loadColorsReference()

    def __baseId(self, id):
        """ Returns the base ID ; see "docs/Map color table" for more informations
        Params:
            id (string): the map color ID
        Returns:
            integer
        """
        return int(id / 4) * 4 + 2

    def __exists(self, id):
        return self.__baseId(id) in self.__colors

    def __loadColorsReference(self):
        """ Loads the colors reference from a json file
        Raises:
            IOError
        """
        # TODO MLG: find a better way to get the file path
        referenceFilePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')
        referenceFile     = os.path.join(referenceFilePath, 'mapcolors.json')
        data              = json.load(open(referenceFile))

        for element in data['colors']:
            self.__colors[element['id']] = MapColor(
                element['id'],
                element['description'],
                element['red'],
                element['green'],
                element['blue']
            )

        # Raise an error if there is no default value
        if 'default' not in self.__colors:
            raise IOError('No default color found in file ' + referenceFile)

    def isDefaultColor(self, id):
        return not self.__exists(self.__baseId(id))

    def rgb(self, id):
        """ Returns a tuple with red, green and blue values
            If there is no color for the ID, it returns a default RGB combination
        Parameters:
            id (int): the map id
        Returns:
            tuple: RGB values. ex: (126, 2, 74)
        """
        if id == 'default':
            return self.__colors['default'].rgb()

        if not self.__exists(self.__baseId(id)):
            return self.__colors['default'].rgb()

        multiply = [180, 220, 255, 135]
        rgb      = map(lambda color: int(color * multiply[id % 4] / 255), self.__colors[self.__baseId(id)].rgb())

        return tuple(rgb)

    def rgbDefaultColor(self):
        return self.rgb('default')
