from yapsy.IPlugin import IPlugin
from multiprocessing import Process, Manager
import os

class PluginTwo(IPlugin):
    def print_name(self):
        p = Process(target=self.pro, args=())
        p.start()
    
    def pro(self):
        while(1):
            print ("This is TEST Plugin with number")
