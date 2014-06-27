__author__ = 'control'


from yapsy.IPlugin import IPlugin
from multiprocessing import Process, Value, Array
import os
import time



class PluginOne(IPlugin):
    def start_plugin(self,sharedArr,eventQueue,lock,plQueue):
        print('plugin2 started')
        goOn = 1
        i = 0;
        while(goOn):
            try:
                event=plQueue.get()
                if (event==1):
                    print('Plugin2 will exit now')
                    goOn=0
                    eventQueue.put([2, 1])
                    break
                if event == 2:
                    lock.acquire()
                    print("---------------------")
                    for i in range(6):
                        print(sharedArr[i])
                    lock.release()
            except:
                time.sleep(0)
                eventQueue.put([2,2])


