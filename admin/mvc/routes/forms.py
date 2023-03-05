from core.application import admin
from ..controllers import auth, dashboard

admin.add_url_rule("/api/login",
                   view_func=auth.LoginFormHandler.as_view("LoginHandler"))
admin.add_url_rule("/get_cpu_usage",
                   view_func=dashboard.CPUView.as_view("CPUView"))
admin.add_url_rule("/get_memory_usage",
                   view_func=dashboard.MemoryView.as_view("MemoryView"))