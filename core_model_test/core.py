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
    eventQueue2 = Queue()
    sharedArr = Array('i',range(6))

    # Loop round the plugins and start them
    for plugin in manager.getAllPlugins():
        plugin.plugin_object.start_plugin(sharedArr, eventQueue,eventQueue2,lock)


    print ('Core process id:', os.getpid())
    goOn = 1;
    while (goOn):
        event=eventQueue.get()
        if (event==1):
            #stop
            goOn = 0
            for plugin in manager.getAllPlugins():
                plugin.plugin_object.end_plugin()
        if (event==2):
            #new data
            print("---------------------")
            lock.acquire()
            for i in range(6):
                print(sharedArr[i])
            lock.release()


if __name__ == "__main__":
    main()