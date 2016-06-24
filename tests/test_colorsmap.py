# -*- coding: utf-8 -*-

import unittest

from minecrafttools.colorsmap   import ColorsMap
from minecrafttools.coordinates import Coordinates # TODO MLG: use fake classes instead
from minecrafttools.dimensions  import Dimensions # TODO MLG: use fake classes instead

class TestColorsMap(unittest.TestCase):

    def test_id(self):
        coordinates = Coordinates(1, 2)
        dimensions  = Dimensions(3, 4)
        colorsMap   = ColorsMap(
            dimensions,
            2,
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        )
        # in this test case the id is 9
        self.assertEqual(7, colorsMap.id(coordinates))

    def test_height(self):
        coordinates = Coordinates(1, 2)
        dimensions  = Dimensions(3, 4)
        colorsMap   = ColorsMap(
            dimensions,
            2,
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        )
        # in this test case the height is 4
        self.assertEqual(4, colorsMap.height())

    def test_scale(self):
        coordinates = Coordinates(1, 2)
        dimensions  = Dimensions(3, 4)
        colorsMap   = ColorsMap(
            dimensions,
            2,
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        )
        # in this test case the scale is 2
        self.assertEqual(2, colorsMap.scale())

    def test_width(self):
        coordinates = Coordinates(1, 2)
        dimensions  = Dimensions(3, 4)
        colorsMap   = ColorsMap(
            dimensions,
            2,
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        )
        # in this test case the width is 3
        self.assertEqual(3, colorsMap.width())

if __name__ == '__main__':
    unittest.main()
