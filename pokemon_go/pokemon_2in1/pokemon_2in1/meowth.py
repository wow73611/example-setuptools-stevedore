#!/usr/bin/env python
#-*- coding:utf-8 -*-

from pokemon_2in1 import base

class Meowth(base.Pokemo):

    def __init__(self):
        super(Meowth,self).__init__(self.__class__.__name__)

    def catch(self):
        print "[%s] Catch Successfully!" % self.name()
