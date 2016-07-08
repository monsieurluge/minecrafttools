# -*- coding: utf-8 -*-

class IntCoordinates:

    def __init__(self, longitude, latitude):
        self.__latitude  = int(latitude)
        self.__longitude = int(longitude)

    def latitude(self):
        return self.__latitude

    def longitude(self):
        return self.__longitude
