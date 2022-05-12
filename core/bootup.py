from core.managers.logging import LoggingManager, Log
from core.loaders.plugins import PluginLoader
from core.loaders.permissions import PermissionsLoader

from core.database.connect import CpDb
from extentions.cli.responses import CLIResponses

log_manager = LoggingManager()

# Routers


def boot_up():
    # CLI text
    cli_text = CLIResponses()
    cli_text.main_response()

    Log("Initializing routers...", 0)

    # Initialize
    permissions = PermissionsLoader()
    permissions.load_permissions()

    plugins = PluginLoader()

    plugins.initialize_plugins()

    from core.mvc.routes import main


# Routers
