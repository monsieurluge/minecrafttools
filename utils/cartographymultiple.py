# -*- coding: utf-8 -*-

from utils.cartography  import Cartography
from utils.map          import Map

class CartographyMultiple(Cartography):

    def __init__(self, mapsDirectory):
        super().__init__(mapsDirectory)

    def generate(self, outputDirectory):
        """ Generates as many pictures as maps crafted in game
        Params:
            outputDirectory (string): The directory where to store the pictures
        Returns:
            CartographyMultiple
        Raises:
            IOError: If the picture file cannot be created for any reason
        """
        for map in sorted(self._maps, key = lambda map: map.scale()):
            try:
                map.save(outputDirectory)
            except IOError as exception:
                print('[WARNING] Failure when trying to generate the "' + map.name() + '" map : ' + format(exception))

        print('[INFO] Cartography (multiple) successfully generated.')

        return self
