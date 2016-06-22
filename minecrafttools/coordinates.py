# -*- coding: utf-8 -*-

class Coordinates:

    def __init__(self, longitude, latitude):
        self.__longitude = longitude
        self.__latitude  = latitude

    def intValues(self):
        return tuple([
            int(self.__longitude),
            int(self.__latitude)
        ])
