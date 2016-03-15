# coding: utf8

from properties import Properties
from whitelist  import Whitelist
from world      import World

import os

# ------------------------------------------------------------------------------
# TODO : class definition
# ------------------------------------------------------------------------------
class Server:

    # --------------------------------------------------------------------------
    # TODO : method definition
    # --------------------------------------------------------------------------
    def __init__(self, minecraftDirectory):
        self.properties = Properties(os.path.join(minecraftDirectory, 'server.properties'))
        self.whitelist  = Whitelist(os.path.join(minecraftDirectory, 'whitelist.json'))
        self.world      = World(os.path.join(minecraftDirectory, self.properties.valueOf('level-name')))

    # --------------------------------------------------------------------------
    # Generate the cartography for the loaded world, depending on the ingame crafted maps
    #
    # @param string outputDirectory
    # --------------------------------------------------------------------------
    def generateCartography(self, outputDirectory):
        self.world.generateCartography(outputDirectory)
