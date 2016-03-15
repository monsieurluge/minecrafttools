# coding: utf8

from property import Property

import re
import sys

# ------------------------------------------------------------------------------
# TODO : class definition
# ------------------------------------------------------------------------------
class Properties:

    # --------------------------------------------------------------------------
    # TODO : method definition
    # --------------------------------------------------------------------------
    def __init__(self, propertiesPath):
        self.properties = []

        try:
            with open(propertiesPath) as propertiesFile:
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
            self.properties.append(Property(matches.group(1), matches.group(2)))

    # --------------------------------------------------------------------------
    # TODO : method definition
    # --------------------------------------------------------------------------
    def valueOf(self, name):
        for property in self.properties:
            if property.name == name:
                return property.value
        return ''
