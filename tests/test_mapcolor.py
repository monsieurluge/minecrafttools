# -*- coding: utf-8 -*-

import unittest

from minecrafttools.mapcolor import MapColor

class TestMapColor(unittest.TestCase):

    def setUp(self):
        self.__testSubject = MapColor(4, 'test description', '123', 0, 201.45)

    def test_rgb(self):
        self.assertEqual((123, 0, 201), self.__testSubject.rgb())

if __name__ == '__main__':
    unittest.main()
