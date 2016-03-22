# coding: utf8

from utils.server import Server

import json
import os
import sys
import getopt
import user

# ------------------------------------------------------------------------------
# Main script
# Returns usage and stops if wrong arguments were given
# ------------------------------------------------------------------------------
def main(arguments):
    minecraftDirectory  = '~/.minecraft'
    outputDirectory     = '~/.minecraft/cartography'

    # Load the config
    try:
        with open(os.getcwd() + '/config.json') as configFile:
            # Get the config data
            configData          = json.load(configFile)
            minecraftDirectory  = configData['Minecraft directory']
            outputDirectory     = configData['Output directory']
    except IOError as error:
        if error.errno == 2:
            # File not found
            print 'Le fichier de configuration n\'a pas été trouvé. Création automatique.'
            createDefaultConfigFile(minecraftDirectory, outputDirectory)
        elif error.errno == 13:
            # Permission denied
            print 'Le fichier de configuration ne peut pas être lu : ' + error.strerror
            sys.exit(2)

    # Check the launch parameters
    try:
        opts, args = getopt.getopt(arguments, 'hdo:', ['minecraftdirectory=', 'outputdirectory'])
    except getopt.GetoptError as errorMessage:
        print str(errorMessage)
        usage()
        sys.exit(2)

    # Update the config, if necessary
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        if opt in ('-d', '--minecraftdirectory'):
            minecraftDirectory = arg
        if opt in ('-o', '--outputdirectory'):
            outputDirectory = arg

    # Load the server
    server = Server(minecraftDirectory)

    # And generate the cartography
    # server.generateCartography(outputDirectory)

# ------------------------------------------------------------------------------
# Create the default config file
# ------------------------------------------------------------------------------
def createDefaultConfigFile(minecraftDirectory, outputDirectory):
    configFile = open(os.getcwd() + '/config.json', 'w')

    # Write the default config values
    configFile.write(
        '{"Minecraft directory" : "' + minecraftDirectory
            + '","Output directory" : "' + outputDirectory
            + '"}')

    # Then close the file
    configFile.close()

# ------------------------------------------------------------------------------
# Returns the script usage
# ------------------------------------------------------------------------------
def usage():
    print 'Options : [-d|--minecraftdirectory] [-o|--outputdirectory]'

# ------------------------------------------------------------------------------
# Launch the script
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main(sys.argv[1:])
