# -*- coding: utf-8 -*-

import unittest

from minecrafttools.intdimensions import IntDimensions

class TestIntDimensions(unittest.TestCase):

    def setUp(self):
        self.testSubject = IntDimensions("10", 15.123)

    def test_width(self):
        # width is an integer value
        self.assertEqual(10, self.testSubject.width())

    def test_height(self):
        # height is an integer value
        self.assertEqual(15, self.testSubject.height())

if __name__ == '__main__':
    unittest.main()
