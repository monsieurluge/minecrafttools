# A Minecraft tools library, written in Python

This library can be used to:
 - print a cartography based on the in-game crafted maps (80%)
 - manage the server (later)
 - manage the whitelist (later)
 - manage the banned players (later)

## Requirements

 - Python v3.5 or later
 - nbt library

## Installation

Go into the package directory, then run this command:
> python -m pip install .

Soon:
> python -m pip install minecrafttools

## Usage

### Cartography

Command line example:
> python minecrafttools/scripts/cartographer.py -d "/home/minecraft/server/" -o "/home/minecraft/cartography/" -t "unique"

Python interpreter:
> \>\>\> from minecrafttools.scripts import cartographer

> \>\>\> cartographer.generateCartography("/home/minecraft/server/", "/home/minecraft/cartography/", "unique")

## Changelog

See the [CHANGELOG](CHANGELOG.md) file

## Roadmap

See the [Trello board (fr)](https://trello.com/b/wfme7mdc/minecraft-tools-scripts)
