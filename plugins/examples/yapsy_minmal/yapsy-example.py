from yapsy.PluginManager import PluginManager
from multiprocessing import Manager, Value

def main():   
    # Load the plugins from the plugin directory.
    manager = PluginManager()
    manager.setPluginPlaces(["plugins"])
    manager.collectPlugins()
    man = Manager()
    l = man.list(range(2))
    num = Value('i',1)

    # Loop round the plugins and print their names.
    for plugin in manager.getAllPlugins():
        plugin.plugin_object.start_plugin(num)


if __name__ == "__main__":
    main()
