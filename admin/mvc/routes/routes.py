from flask import send_from_directory
from core.application import admin
from admin.mvc.controllers import dashboard, auth, plugins, settings, themes
from defines import BASE_DIR
# from core.configreader import DataBaseConfig

controllers = {}

@admin.route("/admin_stat/<path:filename>")
def admin_static_folder(filename):
    return send_from_directory(f"{BASE_DIR}/admin/template/assets/", filename)


# Main url
admin.add_url_rule("/", view_func=dashboard.MainView.as_view("MainDashboard"))

# Login url
admin.add_url_rule(
    "/login", view_func=auth.LoginAuthView.as_view("AdminLoginForm"))
