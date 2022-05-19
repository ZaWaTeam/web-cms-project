from core.application import admin
from admin.mvc.controllers import dashboard, auth, plugins, settings, themes

controllers = {}

# Main url
admin.add_url_rule("/", view_func=dashboard.MainView.as_view("MainDashboard"))

# Login url
admin.add_url_rule(
    "/login", view_func=auth.LoginAuthView.as_view("AdminLoginForm"))
