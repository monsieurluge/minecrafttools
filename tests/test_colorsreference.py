# -*- coding: utf-8 -*-

import unittest

from minecrafttools.colorsreference import ColorsReference

class TestColorsReference(unittest.TestCase):

    def setUp(self):
        self.__testColorsReference = ColorsReference()

    def test_isDefaultColor_True(self):
        isDefaultColor = self.__testColorsReference.isDefaultColor(123456789)
        # the ID 123456789 doesn't exists in the reference file, so it's used as a default color
        self.assertTrue(isDefaultColor)

    def test_isDefaultColor_False(self):
        isDefaultColor = self.__testColorsReference.isDefaultColor(6)
        # the ID 6 refers to a known rgb combination
        self.assertFalse(isDefaultColor)

    def test_rgb_KnownId(self):
        rgbId4 = self.__testColorsReference.rgb(4)
        # the ID 4 refers to a known rgb combination
        self.assertEqual((88, 124, 38), rgbId4)

    def test_rgb_Default(self):
        rgbDefault = self.__testColorsReference.rgb('default')
        # must return the default rgb color
        self.assertEqual((214, 190, 150), rgbDefault)

    def test_rgb_UnknownId(self):
        rgbWatever = self.__testColorsReference.rgb(1234567890)
        # must return the default rgb color
        self.assertEqual((214, 190, 150), rgbWatever)

    def test_rgbDefaultColor(self):
        rgbDefault = self.__testColorsReference.rgbDefaultColor()
        # must return the default rgb color
        self.assertEqual((214, 190, 150), rgbDefault)

if __name__ == '__main__':
    unittest.main()
