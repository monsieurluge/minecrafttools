# coding: utf-8

from distutils.core import setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name                = 'Minecraft Cartographer',
    version             = '0.0.1',
    description         = 'Simple Minecraft Cartographer',
    long_description    = readme,
    author              = 'Monsieur Luge',
    author_email        = 'monsieurluge@gmail.com',
    url                 = 'https://github.com/MonsieurLuge/minecraft-python-cartographer',
    license             = license,
    packages            = ['minecraftserver', 'minecraftcartographer']
)
