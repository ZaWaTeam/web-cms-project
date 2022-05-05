from core.application import Application, app
from core.managers.logging import LoggingManager, Log
from core.loaders.plugins import PluginLoader

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
    plugins = PluginLoader()
    application = Application()

    plugins.initialize_plugins()

    app.jinja_env.globals.update(application=application)

    from core.mvc.routes import main


boot_up()

# Routers
