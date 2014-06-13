from yapsy.IPlugin import IPlugin
from multiprocessing import Process, Manager
import os

class PluginOne(IPlugin):
    def print_name(self, l):
        print ("This is plugin 1, printing l:",l)

    def start_plugin(self,l):
        print("hallo")
  #      p = Process(target=self.pro, args=(l))
  #      p.start()

   # def pro(self,l):
   #     while(1):
   #         print ("This is plugin 1, printing l:",l)