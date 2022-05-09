from core.controller import Controller
from core.loaders.plugins import PluginLoader
from core.plugins.reader import PluginReader


class PermissionsLoader:
    """
    Load all permissions from core and plugins
    """

    permissions = []

    def __init__(self) -> None:
        self.__core = Controller()
        self.__plugin_laoder = PluginLoader()
        self.__plugin_reader = PluginReader()

    def load_permissions(self):
        """
        Start loading all permissions
        """
        # Core reader
        permissions = self.__core.core_permissions()

        for perms in permissions:
            self.permissions.append(
                {"identy": perms.identy, "description": perms.description})

        # Plugin reader

        active_plugins = self.__plugin_laoder.get_active_plugins()

        for aplugins in active_plugins:
            get_perms = self.__plugin_reader.read_permissions(aplugins)

            if get_perms:
                for plugin_perms in get_perms:
                    self.permissions.append({
                        "identy": plugin_perms.identy,
                        "description": plugin_perms.description
                    })
