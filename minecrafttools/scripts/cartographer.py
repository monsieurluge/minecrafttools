# -*- coding: utf-8 -*-

import json
import os
import sys
import getopt
import datetime

from optparse                           import OptionParser
from minecrafttools.cartographymultiple import CartographyMultiple
from minecrafttools.maps                import Maps
from minecrafttools.server              import Server
from minecrafttools.world               import World

def generateCartography(minecraftDirectory, outputFolder, cartographyType):
    ''' Generates the cartography

    Params:
        minecraftDirectory (string): the directory where the server.properties file is in
        outputDirectory (string):    the directory where to generate the cartography file(s)
        cartographyType (string):    what kind of cartography to generate (unique, multiple, [fragmented])
    '''
    start = datetime.datetime.now()

    if cartographyType == 'multiple':
        cartography = CartographyMultiple(
            Maps(
                World(
                    Server(
                        minecraftDirectory
                    ).worldFolder()
                ).mapsFolder()
            ),
            outputFolder
        )
    # elif cartographyType == 'unique':
    #     cartography = CartographyUnique(maps, outputFolder)
    else:
        raise ValueError('"' + cartographyType + '" is not a valid cartography type')

    try:
        # Server(minecraftDirectory).world().cartography(cartographyType, outputDirectory).save()
        cartography.save()
    except (ValueError, IOError) as exception:
        print('Error when trying to generate the cartography:', format(exception))

    end = datetime.datetime.now()

    print('time spent:', round((end - start) / datetime.timedelta(seconds=1), 2), 's')

def main(arguments):
    ''' Main script for command-line purpose'''
    cartographyType    = 'multiple'
    minecraftDirectory = '~/.minecraft'
    outputDirectory    = '~/.minecraft/cartography'
    parser             = OptionParser()

    parser.add_option(
        "-d",
        "--minecraftdirectory",
        dest = "minecraftdirectory",
        help = "directory in where is the server.properties")
    parser.add_option(
        "-o",
        "--outputdirectory",
        dest = "outputdirectory",
        help = "directory where to store the cartography files")
    parser.add_option(
        "-t",
        "--cartographytype",
        dest = "cartographytype",
        help = "kind of cartography to generate (unique, multiple or fragmented)",
        default = "unique")

    # get the command line arguments
    (options, arguments) = parser.parse_args()

    if options.minecraftdirectory:
        minecraftDirectory = options.minecraftdirectory
    if options.outputdirectory:
        outputDirectory = options.outputdirectory
    if options.cartographytype:
        cartographyType = options.cartographytype

    # and generate the cartography
    generateCartography(minecraftDirectory, outputDirectory, cartographyType)

''' Launch the script / command-line usage'''
if __name__ == "__main__":
    main(sys.argv[1:])
