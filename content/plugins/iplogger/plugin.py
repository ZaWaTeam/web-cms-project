from core.managers.plugins import PluginGeneric
from core.plugins.generic import *


class Plugin(PluginGeneric):

    # This function calles when plugin is loaded and ready to work
    def on_ready(self):
        Debug.success("Plugin IPLOGGER successfully activated!")

    # This function called when somebody makes request to the server.
    # This function runs even if user makes request to static files like: Styles, Scripts and Images too.
    def on_request(self, request):
        Debug.success(f"Request has been catched, {request.path}")

    # This function called when request was maden.
    # But this method will be called if request was made not for static files and media files
    def on_fixedrequest(self, request):
        Debug.success(f"Request affored: {request.path}")

    # This function will be callen when administrator from WEBCMS admin disables plugin
    def on_disable(self):
        Debug.warning(
            "Plugin IPLOGGER successfully deactivated. GoodBye!")

    # This function will be callen when administrator deletes this plugin
    def on_delete(self):
        pass
