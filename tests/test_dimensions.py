# -*- coding: utf-8 -*-

import unittest

from minecrafttools.dimensions import Dimensions

class TestDimensions(unittest.TestCase):

    def test_intValues(self):
        dimensions = Dimensions("10", 15.123)
        # dimensions are always integer values
        self.assertEqual((10, 15), dimensions.intValues())

if __name__ == '__main__':
    unittest.main()
