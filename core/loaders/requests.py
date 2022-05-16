"""
## Request handler.

Handle before request and after requests.
"""
from flask import request
from core.application import app
from core.theme_app import Application
from core.managers.auth import user

# Managers
user_manager = user.UserManagement()


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


# @app.after_request
# def handle_after():
#     pass
