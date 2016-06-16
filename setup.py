# -*- coding: utf-8 -*-

from codecs     import open
from os         import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as readme:
    readmeContent = readme.read()

with open(path.join(here, 'LICENSE.txt'), encoding='utf-8') as license:
    licenseContent = license.read()

setup(
    name                = 'minecrafttools',
    version             = '0.1.2',
    description         = 'Minecraft Server Tools',
    long_description    = readmeContent,
    author              = 'Monsieur Luge',
    author_email        = 'monsieurluge@gmail.com',
    url                 = 'https://github.com/MonsieurLuge/minecrafttools',
    license             = licenseContent,
    classifiers         = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    keywords            = 'minecraft tools development',
    packages            = ['minecrafttools', 'minecrafttools.scripts'],
    install_requires    = ['nbt', 'pillow'],
    package_data        = {
        'minecrafttools': ['data/mapcolors.json'],
    }
)
