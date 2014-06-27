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
    Pl2queue = Queue()

    plqueues = [Pl2queue, Pl1queue]

    # shared memory array, represents buffer in core process
    # needs a organisation with lists later
    sharedArr = Array('i',range(6))

    # Loop round the plugins and start them
    i = 0
    p = []
    for plugin in manager.getAllPlugins():
        # spawn new process for plugin. Process uses plugin_start as an entry point
        # Parameter minimum: core queue, plugin queue, buffer
        p.append( Process(target=plugin.plugin_object.start_plugin, args=(sharedArr, eventQueue,lock,plqueues[i]) ) )

        # start the plugin process
        p[i].start()
        i += 1



    # loop for core to wait and polling event queue
    # event definition for core:
    # [x,1]: plugin will quit, please join process -> in this example 1 pl quits means that core will end
    # [x,2]: plugin placed new data in the buffer. please collect
    goOn = 1;
    while goOn:
        # blocking till there is a element to get form queue
        # blocking is no active waiting -> low cpu usage
        event = eventQueue.get()
        #print("Core: got event ",event[1]," from plugin ", event[0])
        if event[1] == 1:
            #stop
            if event[0] == 1:
                Pl2queue.put(1)
                p[0].join()
                print('plugin1 joined')
            if event[0] == 2:
                p[1].join()
                print('plugin2 joined')
                goOn = 0


        if event[1] == 2:
            if event[0] == 1:
                # new data from plugin 1: producer
                #print("Core: transmit new data")
                Pl2queue.put(2)

    # prints this debug message when core process finished/exits
    print("Core finished")


if __name__ == "__main__":
    main()