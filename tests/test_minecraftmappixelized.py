# -*- coding: utf-8 -*-

import unittest

from minecrafttools.colorsmap             import ColorsMap
from minecrafttools.intcoordinates        import IntCoordinates
from minecrafttools.intdimensions         import IntDimensions
from minecrafttools.minecraftmap          import MinecraftMap
from minecrafttools.minecraftmappixelized import MinecraftMapPixelized

class TestMinecraftMap(unittest.TestCase):

    def setUp(self):
        self.expectedCoordinates = IntCoordinates(-129, 361)
        self.expectedDimensions  = IntDimensions(8, 12)
        self.testSubject         = MinecraftMapPixelized(
            MinecraftMap(
                0,
                IntCoordinates(-125, 367),
                ColorsMap(
                    IntDimensions(2, 3),
                    2,
                    [0, 1, 2, 3, 4, 5]
                )
            )
        )

    def test_coordinates(self):
        # longitude
        self.assertEqual(
            self.expectedCoordinates.longitude(),
            self.testSubject.coordinates().longitude()
        )
        # latitude
        self.assertEqual(
            self.expectedCoordinates.latitude(),
            self.testSubject.coordinates().latitude()
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
        # id
        self.assertEqual(5, self.testSubject.id(IntCoordinates(7, 11)))

    def test_scale(self):
        # scale
        self.assertEqual(4, self.testSubject.scale())

if __name__ == '__main__':
    unittest.main()
