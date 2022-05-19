from flask.views import View
from flask import render_template
from admin.managers.security import SecurityManager
from defines import PERMISSIONS


class MainView(View):
    """
    ## Dashboard views.

    This is main view which will parse dashboard template or redirect to login page.
    Security included here. Also initailzation security here.

    Args:
        View (FlaskDynamicViews): Gives necessery functionality to render and dispatch requests.
    """

    def dispatch_request(self):

        # Security
        return SecurityManager.permission_or_redirect(PERMISSIONS.LOGIN_TO_PANEL, "/cpanel/login", render_template("panel/dashboard.html"))
