from .crud import create_record, get_record
from core.managers.plugins import PluginGeneric
from core.plugins.generic import *


class Plugin(PluginGeneric):

    # This function calles when plugin is loaded and ready to work
    def on_ready(self):
        Debug.success("Plugin IPLOGGER successfully initialized")

    # This function called when request was made.
    # But this method will be called if request was made not for static files and media files

    def on_fixedrequest(self, request):
        Debug.success(f"request from IP - {request.remote_addr}")

        if not get_record(request.remote_addr):
            create_record(request.remote_addr)

    # This function will be called when administrator from WEBCMS admin disables plugin

    def on_disable(self):
        Debug.warning("Plugin disabled")

    # This function will be called when administrator deletes this plugin
    def on_delete(self):
        pass
