import importlib
import os.path

from core.configparse import config
from core.managers.lang import LanguageManager
from core.managers.logging import LoggingManager, Log
from core.loaders.plugins import PluginLoader
from core.loaders.permissions import PermissionsLoader
from admin import load_panel

from extentions.cli.responses import CLIResponses
import i18n
import pathlib

lm = LanguageManager('cms')
log_manager = LoggingManager()

# Helper class


class WebcmsBootup:
    """
    ## Webcms bootup

    This is helper class which will take place in loading components of app
    This class makes code bit shorter and comfortable to use.
    Commands can be executed step by step.
    """

    @classmethod
    def load_module(cls, module: str):
        """
        ## Load module.

        Method will load module. If you need to load module somewhere deep in code.
        And do not call nothing from module. This method can be useful.

        #### Notice: Current method loads modules only in `core` directory.
        No need to specify `core` in module argument!

        You can call something from module. It's supports it.
        """
        # Check if module starts with core.(import path)
        if module.split(".")[0] == "core":
            # Load module
            Log(f"Bootup module {module} load warning!", 1)
            Log("No need to specify core in path!", 1)
            module_load = importlib.import_module(module)

            return module_load

        # Load core module if module don't has core in start
        module_load = importlib.import_module(f"core.{module}")

        return module_load

    @classmethod
    def load_router(cls, router_name: str):
        """
        ## Load mvc router.

        Method will load router.
        This method makes code much comfortable and stable.
        No need to use `from core.mvc.routes import router`
        You can call this method and specify router filename.

        #### Notice! This method loads from `core.mvc.routes` path!
        Write only filename without extentions and do not use full path.
        """
        # Load mvc router
        try:

            router_load = importlib.import_module(
                f"core.mvc.routes.{router_name}")

            return router_load

        except ModuleNotFoundError:
            return Log(lm.get('bootup_cannot_load_route').format(router_name), 2)

# Bootup function


def boot_up():
    """
    The boot_up function is called when the program is launched. It initializes all of the necessary
    components for the app to run, including loading permissions and plugins.
    If bootup has errors. Firstly it will contain code 0E1x that means bootup damaged.

    :return: None
    """
    # CLI text
    cli_text = CLIResponses()
    cli_text.main_response()
    Log(lm.get('bootup_init'), 0)

    # Initialize
    permissions = PermissionsLoader()
    permissions.load_permissions()

    plugins = PluginLoader()

    plugins.initialize_plugins()

    # Load Control Panel
    load_panel()

    # Module and router boot up...
    WebcmsBootup.load_module("loaders.requests")
    WebcmsBootup.load_module("theme_app")
    WebcmsBootup.load_router("main")
