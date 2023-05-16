from core.application import api
from admin.mvc.controllers import dashboard
# from core.configreader import DataBaseConfig

# Login url
api.add_resource(dashboard.DashboardProvider, "/sysinfo")