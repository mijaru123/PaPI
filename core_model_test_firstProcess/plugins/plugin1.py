__author__ = 'control'


from yapsy.IPlugin import IPlugin
from multiprocessing import Process, Value, Array
import os
import time



class PluginOne(IPlugin):
    def start_plugin(self,l,eventQueue,lock,plQueue):
        goOn = 1
        i = 0;
        while(goOn):
            try:
                event=plQueue.get_nowait()
                if (event==1):
                    goOn=0
                    eventQueue.put(1)
                    break
            except:
                time.sleep(0)

            lock.acquire()
            for n in range(len(l)):
                l[n] = i + n
            lock.release()
            time.sleep(0.1)
            i += 1
            if (i % 2):
                 eventQueue.put(2)

