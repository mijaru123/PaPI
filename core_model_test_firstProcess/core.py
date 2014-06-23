__author__ = 'control'


from yapsy.PluginManager import PluginManager
from multiprocessing import Process, Value, Array, Lock, Queue
import time
import os

def main():
    # Load the plugins from the plugin directory.
    manager = PluginManager()
    manager.setPluginPlaces(["plugins"])
    manager.collectPlugins()

    lock = Lock()

    eventQueue = Queue()
    Pl1queue = Queue()
    sharedArr = Array('i',range(6))

    # Loop round the plugins and start them
    for plugin in manager.getAllPlugins():
        #plugin.plugin_object.start_plugin(sharedArr, eventQueue,lock)
        p = Process(target=plugin.plugin_object.start_plugin, args=(sharedArr, eventQueue,lock,Pl1queue) )
    p.start()

    print ('Core process id:', os.getpid())
    goOn = 1;
    while (goOn):
        event=eventQueue.get()
        if (event==1):
            #stop
            goOn = 0
            p.join()
            print("joined PL")
        if (event==2):
            #new data
            lock.acquire()
            print("---------------------")
            for i in range(6):
                print(sharedArr[i])
            if (sharedArr[1]>6):
                    Pl1queue.put(1)
            lock.release()
    print("Core finished")


if __name__ == "__main__":
    main()