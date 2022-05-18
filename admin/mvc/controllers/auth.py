from flask.views import View, MethodView
from flask import Response, redirect, render_template, request
from admin.managers.security import SecurityManager
from core.managers.auth import user
from defines import PERMISSIONS


class LoginAuthView(View):
    """
    ## Auth views

    LoginView. Will dispatch requests going to admin login route.
    This view will render admin login form and authenticate user.

    Args:
        View (flask.views): This is interface class. Which containes some functions which can be used in parsing view
    """

    def dispatch_request(self):

        return render_template("auth/login.html")


class LoginFormHandler(MethodView):
    """
    ## Auth method views

    LoginFomrHandler. This class taking important role to handle POST login requests.
    This controller will controll handle requests and prop. Checks, if user don't have permissions.
    It will redirect him to main page or access denied page, if theme designer added this page.

    Args:
        MethodView (flask.views): MethodView gives possibility to handle GET, POST, PUT, DELETE requests or more shorter: request handler 
    """
    username: str
    password: str
    user_manager = user.UserManagement()

    def post(self):

        self.username = request.form.get("username")
        self.password = request.form.get("password")

        handler = self.login_handle()

        return handler

    def login_handle(self):

        user_login = self.user_manager.authenticate_user(
            self.username, self.password, redirect("/cpanel"))

        if not user_login:
            return Response("Incorrect auth credentials")

        return SecurityManager.permission_or_respond(PERMISSIONS.LOGIN_TO_PANEL, user_login, user_login)
