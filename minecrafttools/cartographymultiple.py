# -*- coding: utf-8 -*-

import itertools
import os
import sys

from minecrafttools.cartography     import Cartography
from minecrafttools.colorsreference import ColorsReference
from PIL                            import Image, ImageDraw
from minecrafttools.intcoordinates  import IntCoordinates

class CartographyMultiple(Cartography):

    def save(self):
        """ Generates as many pictures as maps crafted in game """
        for mapFile in sorted(self._maps.maps(), key = lambda minecraftmap: minecraftmap.content().scale()):
            minecraftMap = mapFile.content()
            scale        = minecraftMap.scale() + 1
            pictureSize  = (minecraftMap.dimensions().width() * scale, minecraftMap.dimensions().height() * scale)
            picture      = Image.new('RGB', pictureSize, self._colorsReference.rgbDefaultColor())
            draw         = ImageDraw.Draw(picture)

            for height in range(minecraftMap.dimensions().height()):
                for width in range(minecraftMap.dimensions().width()):
                    x       = width * scale
                    y       = height * scale
                    color   = self._colorsReference.rgb(minecraftMap.id(IntCoordinates(width, height)))

                    draw.rectangle([x, y, x + scale - 1, y + scale - 1], fill = color)

            picture.save(os.path.join(self._folder, mapFile.name() + '.png'))

        print('[INFO] Cartography (multiple) successfully generated.')
