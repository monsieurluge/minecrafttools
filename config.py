# coding: utf8

import json, os, sys

class Config:

    directory = os.getcwd()
    fileName = 'config.json'

    def __init__(self):
        self.cartographyName = 'cartography'
        self.minecraftDirectory = '/home/monsieurluge/Documents/Créations/Divers/Minecraft/Server files'
        self.load()

    # Create the config file
    def createDefaultFile(self):
        configFile = open(self.directory + '/config.json', 'w')
        # Write the default config values
        configFile.write(
            '{"default cartography name" : "' + self.cartographyName
                + '","Minecraft directory" : "' + self.minecraftDirectory
                + '"}')
        # Then close the file
        configFile.close()

    def load(self):
        try:
            with open(self.directory + "/" + self.fileName) as configFile:
                configData = json.load(configFile)
                # Get the config data
                self.setCartographyName(configData['default cartography name'])
                self.setMinecraftDirectory(configData['Minecraft directory'])
        except IOError as error:
            if error.errno == 2:
                # File not found
                self.createDefaultFile()
            elif error.errno == 13:
                # Permission denied
                print 'Le fichier de configuration ne peut pas être lu : ' + error.strerror
                sys.exit(2)

    def getCartographyName(self):
        return self.cartographyName

    def getMinecraftDirectory(self):
        return self.minecraftDirectory

    def setCartographyName(self, name):
        self.cartographyName = name
        return self

    def setMinecraftDirectory(self, directory):
        self.minecraftDirectory = directory
        return self
