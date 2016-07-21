# -*- coding: utf-8 -*-

from minecrafttools.colorsreference       import ColorsReference
from minecrafttools.intcoordinates        import IntCoordinates
from minecrafttools.intdimensions         import IntDimensions
from PIL                                  import Image, ImageDraw
from minecrafttools.minecraftmappixelized import MinecraftMapPixelized

import os

class CartographyUnique():

    def __init__(self, maps, folder):
        """ Creates a CartographyUnique object
        Params:
            maps (Maps):     a list of maps
            folder (string): the folder where to store the cartography files
        """
        self.__colorsReference = ColorsReference()
        self.__coordinates     = None # TODO MLG : find the right way to initialize the coordinates
        self.__dimensions      = None # TODO MLG : find the right way to initialize the dimensions
        self.__folder          = folder
        self.__maps            = maps

    def save(self):
        # TODO MLG: it's time to do some refactoring here
        """ Generates a cartography picture from the maps crafted in game
        Params:
            outputDirectory (string): The directory where to store the picture
        Raises:
            IOError: If the picture file cannot be created for any reason
        """
        # first, determine the picture size
        left   = None
        top    = None
        width  = 0
        height = 0

        for mapFile in self.__maps.maps():
            mapPixelized = MinecraftMapPixelized(mapFile.content())

            # move the top coordinate
            if top is None:
                top  = mapPixelized.coordinates().latitude()
            elif top > mapPixelized.coordinates().latitude():
                height += top - mapPixelized.coordinates().latitude()
                top = mapPixelized.coordinates().latitude()

            # move the left coordinate
            if left is None:
                left  = mapPixelized.coordinates().longitude()
            elif left > mapPixelized.coordinates().longitude():
                width += left - mapPixelized.coordinates().longitude()
                left = mapPixelized.coordinates().longitude()

            # increase the vertical size
            if top + height < mapPixelized.coordinates().latitude() + mapPixelized.dimensions().height():
                height += (mapPixelized.coordinates().latitude() + mapPixelized.dimensions().height()) - (top + height)

            # increase the horizontal size
            if left + width < mapPixelized.coordinates().longitude() + mapPixelized.dimensions().width():
                width += (mapPixelized.coordinates().longitude() + mapPixelized.dimensions().width()) - (left + width)

        self.__coordinates = IntCoordinates(left, top) # TODO MLG: move this to the constructor !
        self.__dimensions  = IntDimensions(width, height) # TODO MLG: move this to the constructor !

        # create the picture with a default background color
        picture = Image.new(
            'RGB',
            (self.__dimensions.width(), self.__dimensions.height()),
            self.__colorsReference.rgbDefaultColor()
        )

        draw = ImageDraw.Draw(picture)

        # then, draw the in-game crafted maps into the picture
        for mapFile in sorted(self.__maps.maps(), key = lambda mapFile: (mapFile.content().scale(), -1 * mapFile.lastModification()), reverse = True):
            mapPixelized = MinecraftMapPixelized(mapFile.content())
            offsetX      = mapPixelized.coordinates().longitude() - self.__coordinates.longitude()
            offsetY      = mapPixelized.coordinates().latitude() - self.__coordinates.latitude()

            for y in range(0, mapPixelized.dimensions().height(), mapPixelized.scale()):
                for x in range(0, mapPixelized.dimensions().width(), mapPixelized.scale()):
                    colorId = mapPixelized.id(IntCoordinates(x, y))

                    # don't draw anything if the color id is the default color
                    if self.__colorsReference.isDefaultColor(colorId):
                        continue

                    draw.rectangle(
                        [
                            offsetX + x, offsetY + y, offsetX + x + mapPixelized.scale(), offsetY + y + mapPixelized.scale()
                        ],
                        fill = self.__colorsReference.rgb(colorId)
                    )

        picture.save(os.path.join(self.__folder, 'cartography.png'))

        print('[INFO] Cartography (unique) successfully generated.')
