# -*- coding: utf-8 -*-

class Player:

    """ TODO class definition """

    def __init__(self, id, name, whitelisted = True, banned = False):
        self.__name           = name
        self.__id             = id
        self.__whitelisted    = whitelisted
        self.__banned         = banned
