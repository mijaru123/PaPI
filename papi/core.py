__author__ = 'control'


from yapsy.PluginManager import PluginManager
from multiprocessing import Process, Value, Array, Lock, Queue
import time
import os
#import gui

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

    # event queue of plugin1 for getting events from core process or gui
    IOPQueue = Queue()
    CoreQueue = Queue()
    GUIQueue = Queue()


    # shared memory array, represents buffer in core process
    sharedArr_time = Array('d',range(100))
    sharedArr_value = Array('d',range(100))



    plugin = manager.getPluginByName('IOP1')
    IOPProcess =  Process(target=plugin.plugin_object.start_plugin, args=(CoreQueue,IOPQueue,sharedArr_time,sharedArr_value,lock) )
    IOPProcess.start();



    #GUIProcess = Process(target=startGUI  , args=(CoreQueue,GUIQueue,sharedArr_time,sharedArr_value,lock))
    #GUIProcess.start()

    # loop for core to wait and polling event queue
    # event definition for core:
    # [x,1]: plugin will quit, please join process -> in this example 1 pl quits means that core will end
    # [x,2]: plugin placed new data in the buffer. please collect
    goOn = 1;
    IOPalive = 1;
    GUIalive = 1;

    while goOn:
        # blocking till there is a element to get form queue
        # blocking is no active waiting -> low cpu usage
        event = CoreQueue.get()
        #print("Core: got event ",event[1]," from plugin ", event[0])
        if event[0] == 'IOP':
            if event[1] == 'Data':
                # new Data available, notice GUI
                GUIQueue.put(['Core','Data'])
                print('Core: new Data, notice GUI')

            if event[1] == 'EndJoin':
                # IOP will end, join process
                print('Core: IOP initiated termination')
                IOPProcess.join()
                IOPalive = 0

            if event[1] == 'Join':
                # IOP needs join
                print('Core: IOP ended and needs a join')
                IOPProcess.join()
                IOPalive = 0

        if event[0] == 'GUI':
            if event[1] == 'Join':
                # join the GUI
                print('Core: GUI ended and needs a join')
                # GUIProcess.join()
                GUIalive = 0

            if event[1] == 'EndJoin':
                # GUI asks for END
                print('Core: GUI initiated termination')
                IOPQueue.put(['Core','End'])
                # GUIProcess.join()
                GUIalive = 0

        goOn = GUIalive | IOPalive

    # prints this debug message when core process finished/exits
    print("Core: Core is finished")


if __name__ == "__main__":
    main()