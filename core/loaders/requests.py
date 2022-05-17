"""
## Request handler.

Handle before request and after requests.
"""
from flask import request
from core.application import app
from core.theme_app import Application
from core.managers.auth import user
from core.loaders.plugins import PluginLoader

# Managers
user_manager = user.UserManagement()

# Loaders
plugin_loader = PluginLoader()


# Requests
@app.before_request
def handle_before():
    # Session checkup
    if user_manager.is_authenticated(request):
        session_checkup = user_manager.session_checkup(request)

        # Get user and set
        usr = user_manager.get_current_user(request)
        setattr(Application, "user", usr)

        return session_checkup

    plugin_loader.call_override("on_request", request=request)

    if "proj_stat" not in request.path.split("/"):
        plugin_loader.call_override("on_fixedrequest", request=request)

# @app.after_request
# def handle_after():
#     pass
