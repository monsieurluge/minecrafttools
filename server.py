# coding: utf8

from player import Player
from world import World

import json
import os
import re
# import string

class Server:

    def __init__(self, minecraftDirectory):
        # Default properties
        self.minecraftDirectory = minecraftDirectory
        self.players = []
        self.properties = {}
        # Some init methods
        self.loadProperties()
        self.loadWhitelist()

    # --------------------------------------------------------------------------
    # Generate the cartography for the loaded world, depending on the ingame crafted maps
    #
    # @param string cartographyName
    # --------------------------------------------------------------------------
    def generateCartography(self, cartographyName):
        self.world.generateCartography(cartographyName)

    # --------------------------------------------------------------------------
    # Load the active world (check server.properties -> levelName property)
    # --------------------------------------------------------------------------
    def loadActiveWorld(self):
        self.world = World(os.path.join(self.minecraftDirectory, self.properties['level-name']))

    # --------------------------------------------------------------------------
    # Load the server properties
    # --------------------------------------------------------------------------
    def loadProperties(self):
        # Try to open the properties file
        try:
            with open(self.minecraftDirectory + '/server.properties') as propertiesFile:
                content = propertiesFile.readlines()
        except IOError as error:
            if error.errno == 2:
                # File not found
                print 'Le fichier de configuration du serveur n\'a pas été trouvé !'
                sys.exit(2)
            elif error.errno == 13:
                # Permission denied
                print 'Le fichier de configuration du serveur ne peut pas être lu : ' + error.strerror
                sys.exit(2)
        # Read and load the property file
        for line in content:
            # Check if the line read is like "property=value"
            matches = re.match('^([a-zA-Z-]+)=(.+)', line)
            if not matches:
                continue
            # Then, save the property & its value
            self.properties[matches.group(1)] = matches.group(2)

    # --------------------------------------------------------------------------
    # Load the whitelist
    # --------------------------------------------------------------------------
    def loadWhitelist(self):
        try:
            with open(os.path.join(self.minecraftDirectory, 'whitelist.json')) as whitelistFile:
                whitelist = json.load(whitelistFile)
        except IOError as error:
            print 'Erreur lors de l\'accès à la whitelist : ' + error.errno
            sys.exit(2)
        # Load the players
        for entry in whitelist:
            player = Player(entry['uuid'], entry['name'])
            self.players.append(player)

    # --------------------------------------------------------------------------
    # Load the active world
    # --------------------------------------------------------------------------
    def loadWorld(self, levelName):
        self.world = World(os.path.join(self.minecraftDirectory, levelName))

    # --------------------------------------------------------------------------
    # Returns the value of the given property name
    # --------------------------------------------------------------------------
    def getProperty(self, propertyName):
        if propertyName in self.properties:
            return self.properties[propertyName]
        return ''
