# -*- coding: utf-8 -*-

import unittest

from minecrafttools.colorsreference import ColorsReference

class TestColorsReference(unittest.TestCase):

    def test_isDefaultColor_True(self):
        colorsReference = ColorsReference()
        isDefaultColor  = colorsReference.isDefaultColor(123456789)
        # the ID 123456789 doesn't exists in the reference file, so it's used as a default color
        self.assertTrue(isDefaultColor)

    def test_isDefaultColor_False(self):
        colorsReference = ColorsReference()
        isDefaultColor  = colorsReference.isDefaultColor(6)
        # the ID 6 refers to a known rgb combination
        self.assertFalse(isDefaultColor)

    def test_rgb_KnownId(self):
        colorsReference = ColorsReference()
        rgbId4          = colorsReference.rgb(4)
        # the ID 4 refers to a known rgb combination
        self.assertEqual((88, 124, 38), rgbId4)

    def test_rgb_Default(self):
        colorsReference = ColorsReference()
        rgbDefault      = colorsReference.rgb('default')
        # must return the default rgb color
        self.assertEqual((214, 190, 150), rgbDefault)

    def test_rgb_UnknownId(self):
        colorsReference = ColorsReference()
        rgbWatever      = colorsReference.rgb(1234567890)
        # must return the default rgb color
        self.assertEqual((214, 190, 150), rgbWatever)

    def test_rgbDefaultColor(self):
        colorsReference = ColorsReference()
        rgbDefault      = colorsReference.rgbDefaultColor()
        # must return the default rgb color
        self.assertEqual((214, 190, 150), rgbDefault)

if __name__ == '__main__':
    unittest.main()
