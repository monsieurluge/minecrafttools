# -*- coding: utf-8 -*-

from utils.mapcolor import MapColor

import json
import os

class ColorsReference:

    def __init__(self):
        self.__colors = {}
        self.__loadColorsReference()

    def __loadColorsReference(self):
        """ Loads the colors reference from a json file

        Raises:
            IOError
        """
        referenceFile = os.path.join(os.path.dirname(__file__), 'map colors.json')
        data          = json.load(open(referenceFile))

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

    def idToRgb(self, id):
        """ Returns a tuple with red, green and blue values
        If there is no color for the ID, it returns a default RGB combination

        Parameters:
            id (int): the map id

        Returns:
            tuple: RGB values. ex: (126, 2, 74)
        """
        if id == 'default':
            return self.__colors['default'].rgb()

        baseId   = int(id / 4) * 4 + 2
        multiply = [180, 220, 255, 135]

        if not baseId in self.__colors:
            return self.__colors['default'].rgb()

        rgb = map(lambda color: int(color * multiply[id % 4] / 255), self.__colors[baseId].rgb())

        return tuple(rgb)
