# -*- coding: utf-8 -*-

from utils.server import Server

import json
import os
import sys
import getopt

# ------------------------------------------------------------------------------
# Main script
# Returns usage and stops if wrong arguments were given
# ------------------------------------------------------------------------------
def main(arguments):
    cartographyType     = 'multiple'
    minecraftDirectory  = '~/.minecraft'
    outputDirectory     = '~/.minecraft/cartography'

    # Load the config
    try:
        with open(os.path.join(os.getcwd(), 'data', 'config.json')) as configFile:
            # Get the config data
            configData          = json.load(configFile)
            cartographyType     = configData['Cartography type']
            minecraftDirectory  = configData['Minecraft directory']
            outputDirectory     = configData['Output directory']
    except IOError as error:
        if error.errno == 2:
            # File not found
            print('[WARNING] The default configuration file was not found.')
            createDefaultConfigFile(minecraftDirectory, outputDirectory, cartographyType)
            sys.exit(1)
        elif error.errno == 13:
            # Permission denied
            print('[ERROR] Error when trying to read the configuration file : "' + error.strerror + '"')
            sys.exit(2)

    # Check the launch parameters
    try:
        opts, args = getopt.getopt(arguments, 'hdoc:', ['minecraftdirectory', 'outputdirectory', 'cartographytype'])
    except getopt.GetoptError as errorMessage:
        print(str(errorMessage))
        usage()
        sys.exit(2)

    # Get the command line arguments, and overwrite the config if necessary
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        if opt in ('-d', '--minecraftdirectory'):
            minecraftDirectory = arg
        if opt in ('-o', '--outputdirectory'):
            outputDirectory = arg
        if opt in ('-c', '--cartographytype'):
            cartographyType = arg

    # Load the server
    server = Server(minecraftDirectory)

    # And generate the cartography
    server.world().cartography().generate(outputDirectory, cartographyType)

# ------------------------------------------------------------------------------
# Creates the default config file
# ------------------------------------------------------------------------------
def createDefaultConfigFile(minecraftDirectory, outputDirectory, cartographyType):
    configPath = os.path.join(os.getcwd(), 'data', 'config.json')
    configFile = open(configPath, 'w')

    # Write the default config values
    configFile.write(
        '{"Minecraft directory" : "' + minecraftDirectory
            + '","Output directory" : "' + outputDirectory
            + '","Cartography type" : "' + cartographyType
            + '"}')

    # Then close the file
    configFile.close()
    print('[INFO] A default configuration file was generated:\n' + configPath +'\nPlease restart this script')

# ------------------------------------------------------------------------------
# Returns the script usage
# ------------------------------------------------------------------------------
def usage():
    # TODO Better usage helper
    print('Options : [-d|--minecraftdirectory] [-o|--outputdirectory] [-c|--cartographytype]')

# ------------------------------------------------------------------------------
# Launch the script
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main(sys.argv[1:])
