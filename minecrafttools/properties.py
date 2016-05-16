# -*- coding: utf-8 -*-

from minecrafttools.property import Property

import re
import sys

class Properties:

    def __init__(self, propertiesPath):
        self.__properties = []

        try:
            with open(propertiesPath) as propertiesFile:
                content = propertiesFile.readlines()
        except IOError as error:
            if error.errno == 2:
                # File not found
                print('[ERROR] The server\'s configuration file was not found : "' + propertiesPath + '"')
                sys.exit(2)
            elif error.errno == 13:
                # Permission denied
                print('[ERROR] The server\'s configuration file is not readable: "' + error.strerror + '"')
                sys.exit(2)

        # Read and load the property file
        for line in content:
            # Check if the line read is like "property=value"
            matches = re.match('^([a-zA-Z-]+)=(.+)', line)
            if not matches:
                continue
            # Then, save the property & its value
            self.__properties.append(Property(matches.group(1), matches.group(2)))

    def valueOf(self, name):
        """ Returns the value of the named property
        Params:
            name (string): The name of the property
        Returns:
            string: The value of the property, empty string if the property doesn't exist
        """
        for property in self.__properties:
            if property.name() == name:
                return property.value()
        return ''
