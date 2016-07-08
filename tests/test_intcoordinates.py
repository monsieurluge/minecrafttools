# -*- coding: utf-8 -*-

import unittest

from minecrafttools.intcoordinates import IntCoordinates

class TestIntCoordinates(unittest.TestCase):

    def setUp(self):
        self.__coordinates = IntCoordinates("10", 15.123)

    def test_latitude(self):
        # latitude is an integer value
        self.assertEqual((15), self.__coordinates.latitude())

    def test_longitude(self):
        # longitude is an integer value
        self.assertEqual((10), self.__coordinates.longitude())

if __name__ == '__main__':
    unittest.main()
