#!/usr/bin/env python
#-*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "pokemon_2in1",
    version = "0.1",
    packages = find_packages(),
    entry_points = {
        'pokemon': [
            'meowth = pokemon_2in1.meowth:Meowth',
            'pikachu = pokemon_2in1.pikachu:Pikachu',
        ],
        'pokemon_2in1': [
            'meowth = pokemon_2in1.meowth:Meowth',
            'pikachu = pokemon_2in1.pikachu:Pikachu',
        ],
        'pokemon_default': [
            'default = pokemon_2in1.pikachu:Pikachu',
        ]
    }
)
