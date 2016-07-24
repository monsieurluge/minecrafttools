# -*- coding: utf-8 -*-

from minecrafttools.cartographycoordinates import CartographyCoordinates
from minecrafttools.cartographydimensions  import CartographyDimensions
from minecrafttools.colorsreference        import ColorsReference
from minecrafttools.intcoordinates         import IntCoordinates
from minecrafttools.intdimensions          import IntDimensions
from PIL                                   import Image, ImageDraw
from minecrafttools.minecraftmappixelized  import MinecraftMapPixelized

import os

class CartographyUnique():

    def __init__(self, maps, folder):
        """ Creates a CartographyUnique object
        Params:
            maps (Maps):     a list of maps
            folder (string): the folder where to store the cartography files
        """
        self.__colorsReference = ColorsReference()
        self.__coordinates     = CartographyCoordinates(maps)
        self.__dimensions      = CartographyDimensions(maps)
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
