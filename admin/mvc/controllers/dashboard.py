from flask.views import View
from flask import render_template, request
from admin.managers.security import SecurityManager
from defines import PERMISSIONS
from core.managers.auth import user


class MainView(View):
    """
    ## Dashboard views.

    This is main view which will parse dashboard template or redirect to login page.
    Security included here. Also initailzation security here.

    Args:
        View (FlaskDynamicViews): Gives necessery functionality to render and dispatch requests.
    """
    user_manager = user.UserManagement()

    def dispatch_request(self):

        context = {
            "title": "Dashboard | PyCMS",
            "user": self.user_manager.get_current_user(request),
            "request": request
        }

        # Security
        return SecurityManager.permission_or_redirect(PERMISSIONS.LOGIN_TO_PANEL, "/cpanel/login", render_template("panel/dashboard.html", **context))
