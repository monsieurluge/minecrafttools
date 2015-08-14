# coding: utf8

from server import Server
from config import Config

import sys, getopt

# ------------------------------------------------------------------------------
# Main script
# Returns usage and stops if wrong arguments were given
# ------------------------------------------------------------------------------
def main(arguments):
    # Load the config
    config = Config()

    # Check the launch parameters
    try:
        opts, args = getopt.getopt(arguments, 'hcd:', ['cartographyname=', 'minecraftdirectory='])
    except getopt.GetoptError as errorMessage:
        print str(errorMessage)
        usage()
        sys.exit(2)

    # Update the config, if necessary
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        if opt in ('-c', '--cartographyname'):
            config.setCartographyName(arg)
        if opt in ('-d', '--minecraftdirectory'):
            config.setMinecraftDirectory(arg)

    # Load the server
    server = Server(config.getMinecraftDirectory())
    server.loadActiveWorld()

    # And generate the cartography
    server.generateCartography(config.getCartographyName())

# ------------------------------------------------------------------------------
# Returns the script usage
# ------------------------------------------------------------------------------
def usage():
    print 'Options : [-c|--cartographyname] [-d|--minecraftdirectory]'

# ------------------------------------------------------------------------------
# Launch the script
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main(sys.argv[1:])
