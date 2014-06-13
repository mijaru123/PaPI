from yapsy.IPlugin import IPlugin
from multiprocessing import Process, Manager
import os

class PluginTwo(IPlugin):
    def pro(self,l):
        while(1):
           # print ("This is TEST Plugin with number")
            print(l.value)


    def print_name(self,l):
        #p = Process(target=self.pro, args=())
        #p.start()
        print(l)

    def start_plugin(self,l):
        print(l)
        p = Process(target=self.pro, args=(l,) )
        p.start()
    
