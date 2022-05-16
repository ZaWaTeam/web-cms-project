from core.managers.logging import LoggingManager, Log
from core.loaders.plugins import PluginLoader
from core.loaders.permissions import PermissionsLoader

from extentions.cli.responses import CLIResponses

log_manager = LoggingManager()

# Routers


def boot_up():
    """
    The boot_up function is called when the program is launched. It initializes all of the necessary
    components for the app to run, including loading permissions and plugins.

    :return: None
    """
    # CLI text
    cli_text = CLIResponses()
    cli_text.main_response()

    Log("Initializing routers...", 0)

    # Initialize
    permissions = PermissionsLoader()
    permissions.load_permissions()

    plugins = PluginLoader()

    plugins.initialize_plugins()

    from core.loaders import requests
    from core import theme_app
    from core.mvc.routes import main


# Routers
