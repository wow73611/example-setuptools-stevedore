#!/usr/bin/env python
#-*- coding:utf-8 -*-

import abc
import six

@six.add_metaclass(abc.ABCMeta)
class Pokemo:

  def __init__(self, name):
      self._name = name

  def name(self):
      return self._name

  @abc.abstractmethod
  def catch(self):
      pass
