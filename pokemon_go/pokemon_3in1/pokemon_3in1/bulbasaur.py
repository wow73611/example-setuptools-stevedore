#!/usr/bin/env python
#-*- coding:utf-8 -*-

from pokemon_3in1 import base

class Bulbasaur(base.Pokemo):
    def __init__(self):
        super(Bulbasaur,self).__init__(self.__class__.__name__)

    def catch(self):
        print "[%s] Catch Successfully!" % self.name()
