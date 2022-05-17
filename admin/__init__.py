"""
WEBCMS CONTROL PANEL
"""
import importlib

from core.managers.logging import Log


class WebcmsAdmin:
    """
    ## WEBCMS ADMIN

    This is helper class to load and handle panels functions.
    It's includes manager loader, loader and other functionality and extentions

    Commands will be completed step by step.
    """
    # Managers variable. Stores list of managers

    @classmethod
    def load_mvc_router(cls, router_name: str):
        """
        ## Load Routes

        Method load_mvc_router(router_name: str) belongs to WebcmsAdmin.
        Method loads routers of mvc directory. It will replace `from admin.mvc import router`
        """
        get_router = importlib.import_module(f"admin.mvc.{router_name}")

        # Log executed code
        Log(f"Sucessfully initialized admin route: \"{router_name}\"", 3)

        return get_router

    @classmethod
    def load_module(cls, module: str):
        """
        ## Load module.

        Method will load module. If you need to load module somewhere deep in code.
        And do not call nothing from module. This method can be useful.

        #### Notice: Current method loads modules only in `admin` directory.
        No need to specify `admin` in module argument!

        You can call something from module. It's supports it.
        """
        # Check if module starts with admin.(import path)
        if module.split(".")[0] == "admin":
            # Load module
            Log(f"Module {module} load warning!", 1)
            Log("No need to specify admin!", 1)
            module_load = importlib.import_module(module)

            return module_load

        # Load admin module if module don't has admin in start
        module_load = importlib.import_module(f"admin.{module}")

        return module_load


def load_panel():
    """
    ## Initialize and load control panel.

    When this function called. It will load all admin panel classes, extentions, functions and themes
    Panel includes own loaders and manager, which will be loaded with this function.
    All you need to do, call this magical function in `core/bootup.py` and everything is done.
    """
    WebcmsAdmin.load_mvc_router("routes")
