#!/usr/bin/env python
#-*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "pokemon_3in1",
    version = "0.1",
    packages = find_packages(),
    entry_points = {
        'pokemon': [
            'bulbasaur = pokemon_3in1.bulbasaur:Bulbasaur',
            'charmander = pokemon_3in1.charmander:Charmander',
            'squirtle = pokemon_3in1.squirtle:Squirtle',
        ],
        'pokemon_3in1': [
            'bulbasaur = pokemon_3in1.bulbasaur:Bulbasaur',
            'charmander = pokemon_3in1.charmander:Charmander',
            'squirtle = pokemon_3in1.squirtle:Squirtle',
        ],
        'pokemon_default': [
            'default = pokemon_3in1.squirtle:Squirtle',
        ]
    }
)
