__author__ = 'control'


from yapsy.PluginManager import PluginManager
from multiprocessing import Process, Value, Array, Lock, Queue
import time
import os

def main():
    # for better process tracking, print process ID of core process
    print('Core process id:', os.getpid())

    # Load the plugins from the plugin directory.
    # prepare plugin manager for dir 'plugins'
    manager = PluginManager()
    manager.setPluginPlaces(["plugins"])
    manager.collectPlugins()


    # create a lock object for mutex usage
    lock = Lock()

    # event queue of core process for getting events from plugins or gui
    eventQueue = Queue()

    # event queue of plugin1 for getting events from core process or gui
    # first approach: plugin queue in core
    # idea: maybe put plugin queue in each plugin process to better memory management
    Pl1queue = Queue()

    # shared memory array, represents buffer in core process
    # needs a organisation with lists later
    sharedArr = Array('i',range(6))

    # Loop round the plugins and start them
    for plugin in manager.getAllPlugins():
        # spawn new process for plugin. Process uses plugin_start as an entry point
        # Parameter minimum: core queue, plugin queue, buffer
        p = Process(target=plugin.plugin_object.start_plugin, args=(sharedArr, eventQueue,lock,Pl1queue) )

        # start the plugin process
        p.start()

    # loop for core to wait and polling event queue
    # event definition for core:
    # 1: plugin will quit, please join process -> in this example 1 pl quits means that core will end
    # 2: plugin placed new data in the buffer. please collect
    goOn = 1;
    while goOn:
        # blocking till there is a element to get form queue
        # blocking is no active waiting -> low cpu usage
        event = eventQueue.get()

        if event == 1:
            #stop
            goOn = 0
            p.join()
            print("joined PL")

        if event == 2:
            # lock before reading buffer
            # to reduce time inside the lock, maybe copy the buffer and then perform operations on the data
            lock.acquire()
            print("---------------------")
            for i in range(6):
                print(sharedArr[i])
            if sharedArr[1] > 6 :
                    Pl1queue.put(1)
            # unlock after reading buffer
            lock.release()


    # prints this debug message when core process finished/exits
    print("Core finished")


if __name__ == "__main__":
    main()