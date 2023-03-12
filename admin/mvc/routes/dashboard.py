from flask import send_from_directory
from core.application import api
from admin.mvc.controllers import dashboard
from defines import BASE_DIR
# from core.configreader import DataBaseConfig

# Login url
api.add_resource(dashboard.DashboardProvider, "/sysinfo")