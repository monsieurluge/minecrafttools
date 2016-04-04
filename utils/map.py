# -*- coding: utf-8 -*-

class Map:

    """ TODO class definition """

    def __init__(self, name, scale, dimension, width, height, xCenter, zCenter, colors):
        self.__name       = name
        self.__scale      = int(scale)
        self.__dimension  = int(dimension)
        self.__width      = int(width)
        self.__height     = int(height)
        self.__xCenter    = xCenter
        self.__zCenter    = zCenter
        self.__colors     = colors

    def name(self):
        """ Return the map name

        Returns:
            string
        """
        return self.__name

    def save(self, directory, colorsReference):
        """ Save the map to a picture file (.png)

        Params:
            directory (string):     directory where to save the file
            colorsReference (dict): reference between the map colors and the RGB colors

        Returns:
            Map

        Raises:
            IOError: If the file cannot be written for any reason
        """
        # for color in self.__colors:
        #     pass

        return self

    def scale(self):
        """ Return the map scale

        Returns:
            integer
        """
        return self.__scale
