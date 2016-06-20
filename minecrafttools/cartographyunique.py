# -*- coding: utf-8 -*-

from minecrafttools.cartography     import Cartography
from minecrafttools.colorsreference import ColorsReference
from minecrafttools.coordinates     import Coordinates
from minecrafttools.dimensions      import Dimensions
from minecrafttools.map             import Map
from PIL                            import Image, ImageDraw

import os

class CartographyUnique(Cartography):

    def __init__(self, mapsDirectory):
        super().__init__(mapsDirectory)

    def generateInto(self, outputDirectory):
        # TODO MLG: it's time to do some refactoring here
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
        left   = None
        top    = None
        width  = 0
        height = 0

        for map in self._maps:
            # move the top coordinate
            if top is None:
                top  = map.top()
            elif top > map.top():
                height += top - map.top()
                top = map.top()

            # move the left coordinate
            if left is None:
                left  = map.left()
            elif left > map.left():
                width += left - map.left()
                left = map.left()

            # increase the vertical size
            if top + height < map.top() + map.heightInPixels():
                height += (map.top() + map.heightInPixels()) - (top + height)

            # increase the horizontal size
            if left + width < map.left() + map.widthInPixels():
                width += (map.left() + map.widthInPixels()) - (left + width)

        self._coordinates = Coordinates(left, top) # TODO MLG: move this to the constructor !
        self._dimensions  = Dimensions(width, height) # TODO MLG: move this to the constructor !

        # create the picture with a default background color
        picture = Image.new(
            'RGB',
            (self._dimensions.intValues()[0], self._dimensions.intValues()[1]),
            colorsReference.rgbDefaultColor()
        )

        draw = ImageDraw.Draw(picture)

        # then, draw the in-game crafted maps into the picture
        for map in sorted(self._maps, key = lambda map: (map.scale(), -1 * map.lastModification()), reverse = True):
            map.saveInto(draw, map.left() - self._coordinates.intValues()[0], map.top() - self._coordinates.intValues()[1], colorsReference)

        picture.save(os.path.join(outputDirectory, 'cartography.png'))

        print('[INFO] Cartography (unique) successfully generated.')

        return self
