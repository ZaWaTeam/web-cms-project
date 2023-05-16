from core.application import api
from admin.mvc.controllers import auth
# from core.configreader import DataBaseConfig

# Login url
api.add_resource(auth.AuthenticationProvider, "/login")

# Userinfo url
api.add_resource(auth.UserInfoScopeProvider, "/user")

# Logout url
api.add_resource(auth.AuthenticationLogoutProvider, "/logout")