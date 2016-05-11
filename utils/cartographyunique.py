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

            # top left coordinates
            if self._topLeftCoordinates is None:
                self._topLeftCoordinates = [mapTopLeft[0], mapTopLeft[1]]
            else:
                if self._topLeftCoordinates[0] > mapTopLeft[0]:
                    self._topLeftCoordinates[0] = mapTopLeft[0]
                if self._topLeftCoordinates[1] > mapTopLeft[1]:
                    self._topLeftCoordinates[1] = mapTopLeft[1]

            # width and height
            # TODO Fix that !!
            if mapTopLeft[0] < self._topLeftCoordinates[0]:
                self._horizontalSize += self._topLeftCoordinates[0] - mapTopLeft[0]
            if mapTopLeft[0] + map.widthInPixels() > self._topLeftCoordinates[0] + self._horizontalSize:
                self._horizontalSize += (mapTopLeft[0] + map.widthInPixels()) - (self._topLeftCoordinates[0] + self._horizontalSize)
            if mapTopLeft[1] < self._topLeftCoordinates[1]:
                self._verticalSize += self._topLeftCoordinates[1] - mapTopLeft[1]
            if mapTopLeft[1] + map.heightInPixels() > self._topLeftCoordinates[1] + self._verticalSize:
                self._verticalSize += (mapTopLeft[1] + map.heightInPixels()) - (self._topLeftCoordinates[1] + self._verticalSize)

        picture = Image.new('RGB', (self._horizontalSize, self._verticalSize), colorsReference.idToRgb('default'))
        draw    = ImageDraw.Draw(picture)

        # then, draw the in-game crafted maps into the picture
        for map in sorted(self._maps, key = lambda map: map.scale(), reverse = True):
            xOffset = map.topLeftCoordinates()[0] - self._topLeftCoordinates[0]
            yOffset = map.topLeftCoordinates()[1] - self._topLeftCoordinates[1]
            try:
                map.saveInto(draw, xOffset, yOffset)
            except IOError as exception:
                print('[WARNING] Failure when trying to add the "' + map.name() + '" map to the cartography: ' + format(exception))

        picture.save(os.path.join(outputDirectory, 'cartography.png'))

        print('[INFO] Cartography (unique) successfully generated.')

        return self
