from genericpath import isfile
import os

from core.configreader import DataBaseConfig
from defines import BASE_DIR

class AdminPluginManager:
    """
    ## Admin Plugin Manager

    All needs to manage plugins from control panel
    Functions:
        - Get information about plugin(s)
        - Edit information about plugin(s) (Add, Delete)
        - Disable plugin(s)
        - Enable plugin(s)
    """

    def __init__(self) -> None:
        self.plugins = []
        self.__db = DataBaseConfig()

    def get_available_plugins(self):
        """
        ## Get Available Plugins

        Gets all available plugins from plugins directory list
        """
        # Plugin list
        path = f"{BASE_DIR}/content/plugins"
        pluginlist = os.listdir(path=path)

        for index, item in enumerate(pluginlist):
            if os.path.isdir(path + "/" + item):
                if os.path.exists(path + "/" + item + "/manifest.json"):
                    self.plugins.append({"name": item, "path": path})

        return self.plugins
    
    def get_active_plugins(self):
        """
        ## Get Active Plugins

        Gets all enabled plugins which are in use
        """
        active_plugins_list = self.__db.get_parsed_config("active_plugins")

        return active_plugins_list