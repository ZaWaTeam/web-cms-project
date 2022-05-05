from core.managers.plugins import PluginGeneric
from core.plugins import generic
from flask import request


class Plugin(PluginGeneric):

    def __init__(self) -> None:
        super().__init__()

    # This function calles when plugin is loaded and ready to work
    def on_ready(self):
        generic.Debug.success("Plugin IPLOGGER successfully activated!")

    # This function will be callen when administrator from admin panel disables plugin

    def on_disable(self):
        generic.Debug.warning(
            "Plugin IPLOGGER successfully deactivated. GoodBye!")

    # This function will be callen when administrator deletes this plugin
    def on_delete(self):
        pass
