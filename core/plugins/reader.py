from collections import namedtuple
from genericpath import isdir, isfile
import json
from defines import BASE_DIR


class PluginReader():
    """
    ### Read active plugins manifest
    """
    __plugin_base_dir = "content/plugins"
    __plugin_base_full_dir = f"{BASE_DIR}/content/plugins"

    def read_plugin(self, plugin: str):
        """
        Read plugin manifest
        """
        # If plugin exists in directory defined in __plugin_base_dir
        if not isdir(f"{self.__plugin_base_dir}/{plugin}"):
            return None

        # Path to manifest.json of plugin
        manifest = f"{self.__plugin_base_dir}/{plugin}/manifest.json"

        # If plugin has manifest
        if isfile(manifest):
            # Get data inside manifest.json and parse it
            read_manifest = open(manifest, "r")

            manifest_data = json.load(read_manifest)

            return manifest_data

        # TODO: Add exception, I was too lazy
        raise ValueError

    def read_permissions(self, plugin_name: str):
        """
        Read permission part of plugin manifest
        """
        # Read plugin
        plugin_manifest = self.read_plugin(plugin_name)

        if not plugin_manifest["plugin"]["permissions"]:
            # TODO: Create exception. I was too lazy
            return False

        return plugin_manifest["plugin"]["permissions"]
