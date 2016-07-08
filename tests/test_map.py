# -*- coding: utf-8 -*-

import unittest

from minecrafttools.colorsmap      import ColorsMap
from minecrafttools.intcoordinates import IntCoordinates
from minecrafttools.intdimensions  import IntDimensions
from minecrafttools.minecraftmap   import MinecraftMap

class TestMap(unittest.TestCase):

    def setUp(self):
        self.__testMap = MinecraftMap(
            'test map',
            0,
            IntCoordinates(-125, 367),
            ColorsMap(
                IntDimensions(2, 3),
                2,
                [0, 1, 2, 3, 4, 5]
            ),
            1466769761
        )

    def test_heightInPixels(self):
        # height in pixels is height * pow(2, scale)
        self.assertEqual(12, self.__testMap.heightInPixels())

    def test_lastModification(self):
        # last modification timestamp
        self.assertEqual(1466769761, self.__testMap.lastModification())

    def test_left(self):
        # left coordinate is width/2 pixels left to the center
        self.assertEqual(-129, self.__testMap.left())

    def test_name(self):
        # map name
        self.assertEqual('test map', self.__testMap.name())

    def test_save(self):
        # TODO MLG: map save test
        pass

    def test_saveFragments(self):
        # TODO MLG: map save fragments test
        pass

    def test_saveInto(self):
        # TODO MLG: map save into test
        pass

    def test_scale(self):
        # map scale
        self.assertEqual(2, self.__testMap.scale())

    def test_top(self):
        # top coordinate is height/2 pixels top to the center
        self.assertEqual(361, self.__testMap.top())

    def test_widthInPixels(self):
        # width in pixels is width * pow(2, scale)
        self.assertEqual(8, self.__testMap.widthInPixels())

if __name__ == '__main__':
    unittest.main()
