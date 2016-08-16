#!/usr/bin/env python
#-*- coding:utf-8 -*-

from pokemon_3in1 import base

class Squirtle(base.Pokemo):

    def __init__(self):
        super(Squirtle,self).__init__(self.__class__.__name__)

    def catch(self):
        print "[%s] Catch Successfully!" % self.name()
