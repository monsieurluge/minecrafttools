# coding: utf-8

from distutils.core import setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name                = 'minecrafttools',
    version             = '0.1.0',
    description         = 'Minecraft Tools Library',
    long_description    = readme,
    author              = 'Monsieur Luge',
    author_email        = 'monsieurluge@gmail.com',
    url                 = 'https://github.com/MonsieurLuge/minecrafttools',
    license             = license,
    packages            = ['minecrafttools']
)
