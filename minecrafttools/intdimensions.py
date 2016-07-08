# -*- coding: utf-8 -*-

class IntDimensions:

    def __init__(self, width, height):
        self.__width  = int(width)
        self.__height = int(height)

    def width(self):
        return self.__width

    def height(self):
        return self.__height
