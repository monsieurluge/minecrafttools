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
    version             = '0.1.0',
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
    packages            = ['minecrafttools'],
    install_requires    = ['nbt'],
    package_data        = {
        'data': ['map colors.json']
    }
)
