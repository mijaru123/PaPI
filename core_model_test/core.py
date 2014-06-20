__author__ = 'control'


from yapsy.PluginManager import PluginManager
from multiprocessing import Process, Array


def main():
    # Load the plugins from the plugin directory.
    manager = PluginManager()
    manager.setPluginPlaces(["plugins"])
    manager.collectPlugins()



    sharedArr = Array('i',range(10))

    # Loop round the plugins and start them
    for plugin in manager.getAllPlugins():
        plugin.plugin_object.start_plugin(sharedArr)











if __name__ == "__main__":
    main()