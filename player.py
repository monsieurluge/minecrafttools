# coding: utf8

class Player:

    def __init__(self, id, name, whitelisted = True, banned = False):
        self.name           = name
        self.id             = id
        self.whitelisted    = whitelisted
        self.banned         = banned
