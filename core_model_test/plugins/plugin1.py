__author__ = 'control'


from yapsy.IPlugin import IPlugin
from multiprocessing import Process, Array
import os



class PluginOne(IPlugin):
    def pro(self,l):
        print("Plugin1 Process started")
        while(1):
          l[2] = -1
          #print(l[2])

    def start_plugin(self,l):
        p = Process(target=self.pro, args=(l,) )
        p.start()