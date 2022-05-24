import i18n

from core.managers.lang import LanguageManager
from core.managers.plugins import PluginGeneric
from core.plugins.generic import *

lm = LanguageManager('iplogger')


class Plugin(PluginGeneric):

    # This function calles when plugin is loaded and ready to work
    def on_ready(self):
        Debug.success(lm.get('on_ready'))

    # This function called when somebody makes request to the server.
    # This function runs even if user makes request to static files like: Styles, Scripts and Images too.
    def on_request(self, request):
        Debug.success(lm.get('on_request').format(request.remote_addr))

    # This function called when request was made.
    # But this method will be called if request was made not for static files and media files
    def on_fixedrequest(self, request):
        Debug.success(lm.get('on_fixedrequest').format(request.remote_addr))

    # This function will be called when administrator from WEBCMS admin disables plugin
    def on_disable(self):
        Debug.warning(lm.get('on_disable'))

    # This function will be called when administrator deletes this plugin
    def on_delete(self):
        pass
