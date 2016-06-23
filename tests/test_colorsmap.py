# -*- coding: utf-8 -*-

import unittest

from minecrafttools.colorsmap   import ColorsMap
from minecrafttools.coordinates import Coordinates # TODO MLG: use fake classes instead
from minecrafttools.dimensions  import Dimensions # TODO MLG: use fake classes instead

class TestColorsMap(unittest.TestCase):

    def test_Id(self):
        coordinates = Coordinates(1, 2)
        dimensions  = Dimensions(3, 4)
        colorsMap   = ColorsMap(
            dimensions,
            2,
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        )

        self.assertEqual(9, colorsMap.id(coordinates))

if __name__ == '__main__':
    unittest.main()
