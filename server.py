# coding: utf8

from player import Player
from world import World

import json, re, string

class Server:

    def __init__(self, minecraftDirectory):
        # Default properties
        self.minecraftDirectory = minecraftDirectory
        self.players = []
        # Some init methods
        self.loadProperties()
        self.loadWhitelist()
        self.loadWorld()

    # Now : load some useful properties
    # TODO : load the entire properties set
    def loadProperties(self):
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
        # Read the property file and load some properties
        for line in content:
            matches = re.match('^([a-zA-Z-]+)=(.+)', line)
            if not matches:
                continue
            property = matches.group(1)
            value = matches.group(2)
            try:
                setterName = 'set' + self.propertyNameToCamelCase(property)
                setterMethod = getattr(self, setterName)
            except:
                continue
            setterMethod(value)

    # Load the whitelist
    def loadWhitelist(self):
        try:
            with open(self.minecraftDirectory + '/whitelist.json') as whitelistFile:
                whitelist = json.load(whitelistFile)
        except IOError as error:
            print 'Erreur lors de l\'accès à la whitelist : ' + error.errno
            sys.exit(2)
        # Load the players
        for entry in whitelist:
            player = Player(entry['uuid'], entry['name'])
            self.players.append(player)

    # Load the active world
    def loadWorld(self):
        self.world = World(self.minecraftDirectory + '/' + self.levelName)

    # Format a property name, like level-name, to CamelCase
    def propertyNameToCamelCase(self, propertyName):
        newName = ''
        for element in string.split(propertyName, '-'):
            newName += string.capitalize(element)
        return newName

    def setHardcore(self, value):
        self.hardcore = value

    def setLevelName(self, value):
        self.levelName = value

    def setLevelSeed(self, value):
        self.levelSeed = value

    def setMaxWorldSize(self, value):
        self.maxWorldSize = value

    def setMotd(self, value):
        self.motd = value

    def setSpawnProtection(self, value):
        self.spawnProtection = value
