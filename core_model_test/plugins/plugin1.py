__author__ = 'control'

from papi.papiplugin import PaPIPlugin

from multiprocessing import Process, Value, Array
import os
import time


class PluginOne(PaPIPlugin):

    def custom(self,l,goOn, eventQueue,lock):
        print("Plugin1 Process started")
