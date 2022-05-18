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
    # User checkup
    if user_manager.is_authenticated(request):

        # Get user and set
        usr = user_manager.get_current_user(request)
        setattr(Application, "user", usr)

    else:
        setattr(Application, "user", None)

    plugin_loader.call_override("on_request", request=request)

    if "proj_stat" not in request.path.split("/"):
        plugin_loader.call_override("on_fixedrequest", request=request)


@app.before_request
def session_checkup():
    # Check session in every request
    if "proj_stat" not in request.path.split("/"):
        session_checkup = user_manager.session_checkup(request)

        return session_checkup

# @app.after_request
# def handle_after():
#     pass
