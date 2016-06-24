# -*- coding: utf-8 -*-

import unittest

from minecrafttools.colorsmap   import ColorsMap
from minecrafttools.coordinates import Coordinates # TODO MLG: use fake classes instead
from minecrafttools.dimensions  import Dimensions # TODO MLG: use fake classes instead

class TestColorsMap(unittest.TestCase):

    def setUp(self):
        self.__testColorsMap = ColorsMap(
            Dimensions(3, 4),
            2,
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        )

    def test_id(self):
        # in this test case the id is 9
        self.assertEqual(7, self.__testColorsMap.id(Coordinates(1, 2)))

    def test_height(self):
        # in this test case the height is 4
        self.assertEqual(4, self.__testColorsMap.height())

    def test_scale(self):
        # in this test case the scale is 2
        self.assertEqual(2, self.__testColorsMap.scale())

    def test_width(self):
        # in this test case the width is 3
        self.assertEqual(3, self.__testColorsMap.width())

if __name__ == '__main__':
    unittest.main()
