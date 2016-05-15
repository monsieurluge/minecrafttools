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

        # first, determine the picture size
        for map in self._maps:
            # move the top coordinate
            if self._top is None:
                self._top  = map.top()
            elif self._top > map.top():
                self._verticalSize += self._top - map.top()
                self._top = map.top()
            # move the left coordinate
            if self._left is None:
                self._left  = map.left()
            elif self._left > map.left():
                self._horizontalSize += self._left - map.left()
                self._left = map.left()
            # increase the vertical size
            if self._top + self._verticalSize < map.top() + map.heightInPixels():
                self._verticalSize += (map.top() + map.heightInPixels()) - (self._top + self._verticalSize)
            # increase the horizontal size
            if self._left + self._horizontalSize < map.left() + map.widthInPixels():
                self._horizontalSize += (map.left() + map.widthInPixels()) - (self._left + self._horizontalSize)

        # create the picture with a default background color
        picture = Image.new('RGB', (self._horizontalSize, self._verticalSize), colorsReference.idToRgb('default'))
        draw    = ImageDraw.Draw(picture)

        # then, draw the in-game crafted maps into the picture
        for map in sorted(self._maps, key = lambda map: (map.scale(), -1 * map.lastModification()), reverse = True):
            map.saveInto(draw, map.left() - self._left, map.top() - self._top)

        picture.save(os.path.join(outputDirectory, 'cartography.png'))

        print('[INFO] Cartography (unique) successfully generated.')

        return self
