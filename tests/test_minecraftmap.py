# -*- coding: utf-8 -*-

import unittest

from minecrafttools.colorsmap      import ColorsMap
from minecrafttools.intcoordinates import IntCoordinates
from minecrafttools.intdimensions  import IntDimensions
from minecrafttools.minecraftmap   import MinecraftMap

class TestMinecraftMap(unittest.TestCase):

    def setUp(self):
        self.expectedCoordinates = IntCoordinates(-129, 361)
        self.expectedDimensions  = IntDimensions(2, 3)
        self.testSubject         = MinecraftMap(
            0,
            IntCoordinates(-125, 367),
            ColorsMap(
                IntDimensions(2, 3),
                2,
                [0, 1, 2, 3, 4, 5]
            )
        )

    def test_dimensions(self):
        # height
        self.assertEqual(
            self.expectedDimensions.height(),
            self.testSubject.dimensions().height()
        )
        # width
        self.assertEqual(
            self.expectedDimensions.width(),
            self.testSubject.dimensions().width()
        )

    def test_id(self):
        pass

    def test_scale(self):
        self.assertEqual(2, self.testSubject.scale())

    def test_topLeft(self):
        # longitude
        self.assertEqual(
            self.expectedCoordinates.longitude(),
            self.testSubject.topLeft().longitude()
        )
        # latitude
        self.assertEqual(
            self.expectedCoordinates.latitude(),
            self.testSubject.topLeft().latitude()
        )

if __name__ == '__main__':
    unittest.main()
