# -*- coding: utf-8 -*-

class Coordinates:

    def __init__(self, longitude, latitude):
        self.__longitude = int(longitude)
        self.__latitude  = int(latitude)

    def intValues(self):
        return tuple([
            self.__longitude,
            self.__latitude
        ])
