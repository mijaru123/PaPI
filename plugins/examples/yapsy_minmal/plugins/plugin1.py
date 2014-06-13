from yapsy.IPlugin import IPlugin
from multiprocessing import Process, Manager
import os

class PluginOne(IPlugin):
    def pro(self,l):
        while(1):
           # print ("This is TEST Plugin with number")
            #print(l.value)
          l.value+=1


    def print_name(self,l):
        print(l)

    def start_plugin(self,l):
        print(l)
        p = Process(target=self.pro, args=(l,) )
        p.start()