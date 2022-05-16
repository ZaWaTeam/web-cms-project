from core.managers.plugins import PluginGeneric
from core.plugins import generic


class Plugin(PluginGeneric):

    # This function calles when plugin is loaded and ready to work
    def on_ready(self):
        generic.Debug.success("Plugin IPLOGGER successfully activated!")

    # This function will be callen when administrator from WEBCMS admin disables plugin
    def on_disable(self):
        generic.Debug.warning(
            "Plugin IPLOGGER successfully deactivated. GoodBye!")

    # This function will be callen when administrator deletes this plugin
    def on_delete(self):
        pass
