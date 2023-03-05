import json

from flask.views import View, MethodView
from flask import render_template, request
from admin.managers.security import SecurityManager
from defines import PERMISSIONS
from core.managers.auth import user
from admin.managers.plugins import AdminPluginManager
import psutil


class MainView(View):
    """
    ## Dashboard views.

    This is main view which will parse dashboard template or redirect to login page.
    Security included here. Also initailzation security here.

    Args:
        View (FlaskDynamicViews): Gives necessery functionality to render and dispatch requests.
    """
    user_manager = user.UserManagement()
    plugins = AdminPluginManager()

    def dispatch_request(self):

        memory = psutil.virtual_memory()
        cpu = psutil.cpu_percent()
        disk = psutil.disk_usage('/')
        acitve_plugins, available_plugins = self.plugins.get_active_plugins(), self.plugins.get_available_plugins()

        context = {
            "title": "Dashboard | PyCMS",
            "user": self.user_manager.get_current_user(request),
            "request": request,
            "sysinfo": {
                "memory": memory.percent,
                "cpu": cpu,
                "disk": disk,
                "active_plugins": len(acitve_plugins),
                "available_plugins": len(available_plugins)
            }
        }

        # Security
        return SecurityManager.permission_or_redirect(PERMISSIONS.LOGIN_TO_PANEL, "/cpanel/login", render_template("panel/dashboard.html", **context))

class CPUView(MethodView):
    def dispatch_request(self):
        cpu = psutil.cpu_percent()
        return SecurityManager.permission_or_respond(PERMISSIONS.LOGIN_TO_PANEL, None, json.dumps({"cpu": cpu}))

class MemoryView(MethodView):
    def dispatch_request(self):
        memory = psutil.virtual_memory()
        return SecurityManager.permission_or_respond(PERMISSIONS.LOGIN_TO_PANEL, None, json.dumps({"memory": memory.percent}))