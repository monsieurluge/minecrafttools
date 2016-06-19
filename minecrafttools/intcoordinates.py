# -*- coding: utf-8 -*-

class IntCoordinates:

    def __init__(self, longitude = 0, latitude = 0):
        self.__longitude = longitude
        self.__latitude  = latitude

    def intValues(self):
        return tuple([
            int(self.__longitude),
            int(self.__latitude)
        ])
