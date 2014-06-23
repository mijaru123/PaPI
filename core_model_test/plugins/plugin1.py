__author__ = 'control'


from yapsy.IPlugin import IPlugin
from multiprocessing import Process, Value, Array
import os
import time



class PluginOne(IPlugin):
    def pro(self,l,goOn, eventQueue,lock):
        print("Plugin1 Process started")
        i = 0
        print ('process id:', os.getpid())
        while(goOn.value==1):
            lock.acquire()
            for n in range(len(l)):
                l[n] = i + n
            time.sleep(2)
            lock.release()
            i += 1
            if (i % 2):
                 eventQueue.put(2)
            if ( i > 7 ):
                 eventQueue.put(1)




    def __init__(self):
        self.goOn  = Value('i',0)

    def start_plugin(self,l,eventQueue,lock):
        self.goOn.value =1
        self.p = Process(target=self.pro, args=(l,self.goOn, eventQueue,lock) )
        self.p.start()

    def end_plugin(self):
        self.goOn.value =0
        self.p.join()
        print("Plugin joined")
