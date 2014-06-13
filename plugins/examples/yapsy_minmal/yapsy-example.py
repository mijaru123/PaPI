from yapsy.PluginManager import PluginManager
from multiprocessing import Manager

def main():   
    # Load the plugins from the plugin directory.
    manager = PluginManager()
    manager.setPluginPlaces(["plugins"])
    manager.collectPlugins()
    man = Manager()
    l = man.list(range(2))

    # Loop round the plugins and print their names.
    for plugin in manager.getAllPlugins():
        plugin.plugin_object.start_plugin(l)


if __name__ == "__main__":
    main()
