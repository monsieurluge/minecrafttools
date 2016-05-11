# -*- coding: utf-8 -*-

from utils.cartography      import Cartography
from utils.colorsreference  import ColorsReference
from utils.map              import Map
from PIL                    import Image, ImageDraw

import os

class CartographyUnique(Cartography):

    def __init__(self, mapsDirectory):
        super().__init__(mapsDirectory)

    def generateInto(self, outputDirectory):
        """ Generates a cartography picture from the maps crafted in game
        Params:
            outputDirectory (string): The directory where to store the picture
        Returns:
            CartographyUnique
        Raises:
            IOError: If the picture file cannot be created for any reason
        """
        colorsReference = ColorsReference()

        # TODO: fix the picture size & the map drawing
        # first, determine the picture size
        for map in self._maps:
            mapTopLeft = map.topLeftCoordinates()
            mapScale   = map.scale() + 1

            # top left coordinates
            if self._topLeftCoordinates is None:
                self._topLeftCoordinates = [mapTopLeft[0], mapTopLeft[1]]
            else:
                if self._topLeftCoordinates[0] > mapTopLeft[0]:
                    self._topLeftCoordinates[0] = mapTopLeft[0]
                if self._topLeftCoordinates[1] > mapTopLeft[1]:
                    self._topLeftCoordinates[1] = mapTopLeft[1]

            # width and height
            if mapTopLeft[0] + (map.width() * mapScale) > self._topLeftCoordinates[0] + self._horizontalSize:
                self._horizontalSize = mapTopLeft[0] - self._topLeftCoordinates[0] + (map.width() * mapScale)
            if mapTopLeft[1] + (map.height() * mapScale) > self._topLeftCoordinates[1] + self._verticalSize:
                self._verticalSize = mapTopLeft[1] - self._topLeftCoordinates[1] + (map.height() * mapScale)

        picture = Image.new('RGB', (self._horizontalSize, self._verticalSize), colorsReference.idToRgb('default'))

        # then, draw the in-game crafted maps into the picture
        for map in sorted(self._maps, key = lambda map: map.scale(), reverse = True):
            try:
                xOffset = map.topLeftCoordinates()[0] - self._topLeftCoordinates[0]
                yOffset = map.topLeftCoordinates()[1] - self._topLeftCoordinates[1]
                map.saveInto(picture, xOffset, yOffset)
            except IOError as exception:
                print('[WARNING] Failure when trying to generate the "' + map.name() + '" map : ' + format(exception))

        picture.save(os.path.join(outputDirectory, 'cartography.png'))

        print('[INFO] Cartography (unique) successfully generated.')

        return self
