# -*- coding: utf-8 -*-

class Property:

    """ TODO class definition """

    def __init__(self, name, value):
        self.__name = name
        self.__value = value

    def name(self):
        """ Return the name of the property

        Returns:
            string
        """
        return self.__name

    def value(self):
        """ Returns the value of the property

        Returns:
            string
        """
        return self.__value
