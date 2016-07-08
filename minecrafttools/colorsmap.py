# -*- coding: utf-8 -*-

class ColorsMap:

    def __init__(self, dimensions, scale, colors):
        """ Creates a ColorMap object
        Params:
            dimensions (Dimensions): dimensions of the map
            scale (integer):         scale
            colors (list):           list of colors ID's
        """
        self.__dimensions      = dimensions
        self.__scale           = int(scale)
        self.__colors          = colors

    def id(self, coordinates):
        """ Returns the color ID by its coordinates
        Params:
            coordinates (IntCoordinates): coordinates of the color ID
        Returns:
            integer
        Raises:
            IndexError when the coordinates are out of bound
        """
        index = self.width() * coordinates.latitude() + coordinates.longitude()

        if index > len(self.__colors):
            raise IndexError('these ColorsMap coordinates are out of bound : [' + str(coordinates.longitude()) + ',' + str(coordinates.latitude()) + ']')

        return int(self.__colors[index])

    def height(self):
        """ Returns the height of the map
        Returns:
            integer
        """
        return self.__dimensions.intValues()[1]

    def scale(self):
        """ Returns the scale of the map
        Returns:
            integer
        """
        return self.__scale

    def width(self):
        """ Returns the width of the map
        Returns:
            integer
        """
        return self.__dimensions.intValues()[0]
