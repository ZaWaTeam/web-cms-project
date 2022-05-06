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
            manifest_data = json.load(manifest)

            manifest_converted = namedtuple(
                "ManifestData", manifest_data.keys())(*manifest_data.values())

            return manifest_converted

        raise ValueError
