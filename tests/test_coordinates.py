# -*- coding: utf-8 -*-

import unittest

from minecrafttools.coordinates import Coordinates

class TestCoordinates(unittest.TestCase):

    def test_intValues(self):
        coordinates = Coordinates("10", 15.123)
        # coordinates as integer values
        self.assertEqual((10, 15), coordinates.intValues())

if __name__ == '__main__':
    unittest.main()
