import os
from core.configreader import DataBaseConfig
from importlib import import_module

from core.managers.logging import Log


class PluginLoader():

    __db = DataBaseConfig()

    __plugins = []

    def __init__(self) -> None:
        self.__plugins = []

        self.__plugin_list()

    def __plugin_list(self):
        # Plugin list
        path = f"content/plugins"
        pluginlist = os.listdir(path=path)

        for index, item in enumerate(pluginlist):
            if os.path.isdir(path + "/" + item):
                self.__plugins.append({"name": item, "path": path})

    def __start_plugins(self):
        # Database
        database = self.__db

        database_active_plugins = self.__db.get_parsed_config("active_plugins")

        # Check loop
        for index, d in enumerate(database_active_plugins):
            if self.__dict_finder(self.__plugins, "name", d["name"]) == False:
                del database_active_plugins[index]
                self.__changed_database_plugins(database_active_plugins)

            else:
                self.__initialize_plugin(d["name"], d["path"])

    def __dict_finder(self, plugins, dict_key: str, value):
        filtered = filter(lambda f: f[dict_key] == value, plugins)

        length = bool(len(list(filtered)))

        if length:
            return list(filtered)

        return length

    def __initialize_plugin(self, name, path):

        plugin_module = import_module(f"content.plugins.{name}.plugin")

        plugin = plugin_module.Plugin()

        # issubclass(plugin, PluginGeneric Managment)

        plugin.on_ready()

    def __changed_database_plugins(self, changed_active_plugins):
        database = self.__db
        database.write_parsed_config("active_plugins", changed_active_plugins)

    def __start_override_plugins(self, function_name: str, **arguments):
        # Database
        database = self.__db

        database_active_plugins = self.__db.get_parsed_config("active_plugins")
        directory_active_plugins = self.__plugins
        changed_active_plugins = []

        # Check loop
        for index, d in enumerate(database_active_plugins):
            if self.__dict_finder(self.__plugins, "name", d["name"]) == False:
                del database_active_plugins[index]
                self.__changed_database_plugins(database_active_plugins)

            else:
                self.__call_override_plugin(function_name, **arguments)

    def __call_override_plugin(self, name: str, function_name: str, **arguments):

        plugin_module = import_module(f"content.plugins.{name}.plugin")

        plugin = plugin_module.Plugin()

        # issubclass(plugin, PluginGeneric Managment)

        getattr(plugin, function_name)(**arguments)

    def __changed_database_plugins(self, changed_active_plugins):
        database = self.__db
        database.write_parsed_config("active_plugins", changed_active_plugins)

    """
    * ============== *
      Disable plugin
    * ============== *
    """

    def __disable_plugin(self, name, path):

        plugin_module = import_module(f"content.plugins.{name}.plugin")

        plugin = plugin_module.Plugin()

        # issubclass(plugin, PluginGeneric Managment)

        plugin.on_disable(plugin={"name": name, "path": path})

        # Define database
        database = self.__db

        database_active_plugins = database.get_parsed_config("active_plugins")

        # Check loop
        for d in database_active_plugins:
            if self.__dict_finder(self.__plugins, "name", d["name"]):
                del database_active_plugins[d]
                self.__changed_database_plugins(database_active_plugins)

    """
    * ========================== *
      Accessor to loader.
      --------------------------
      Access modificator: Public
    * ========================== *
    """

    def initialize_plugins(self):
        # Start plugins
        load_plugins = self.__start_plugins()

        return True

    def get_active_plugins(self):
        # Read all active plugins
        database_active_plugins = self.__db.get_parsed_config("active_plugins")
        active_plugins = []

        # Check loop
        for index, d in enumerate(database_active_plugins):
            if self.__dict_finder(self.__plugins, "name", d["name"]) == False:
                del database_active_plugins[index]
                self.__changed_database_plugins(database_active_plugins)

            else:
                active_plugins.append(d["name"])

        return active_plugins

    def call_override(self, function_name: str, **arguments):
        """
        ## Define and call override
        Plugin function will call override method.
        Made for plugin development

        Args:
            function_name (str): name of function which needs to be called
            **arguments: pass arguments which needs to be passed to function
        """
        # Error handler. Catching it here
        try:
            # Code here
            active_plugins = self.get_active_plugins()

            for plugin in active_plugins:
                self.__call_override_plugin(plugin, function_name, **arguments)

        except Exception:
            Log("Plugin loader containes some errors!", 2)
