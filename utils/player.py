# -*- coding: utf-8 -*-

class Player:

    def __init__(self, id, name):
        self.__name           = name
        self.__id             = id

    def id(self):
        """ Returns the player ID
        Returns:
            string
        """
        return self.__id

    def name(self):
        """ Returns the player name
        Returns:
            string
        """
        return self.__name
