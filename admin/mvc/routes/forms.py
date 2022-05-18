from core.application import admin
from ..controllers import auth

admin.add_url_rule("/api/login",
                   view_func=auth.LoginFormHandler.as_view("LoginHandler"))
