from flask import request
from flask_restful import Resource, abort
from admin.managers.security import SecurityManager, SecurityCallback
from core.managers.auth.oauth import OAuth2Manager
from core.managers.exceptions import NotAuthenticated, UserCredsIncorrect, UserNotExists
from core.utils.auth import get_token, has_token
from defines import PERMISSIONS
from playhouse.shortcuts import model_to_dict

class AuthenticationProvider(Resource):
    
    def __init__(self) -> None:
        super().__init__()
        self.manager = OAuth2Manager()
        self.security = SecurityManager()
        self.SCB = SecurityCallback
    
    def post(self):
        username = request.form["username"]
        password = request.form["password"]

        try:
            token, lifetime = self.manager.authenticate(username, password)

        except UserNotExists:
            abort(403, message="Incorrect authentication credentials")
        
        except UserCredsIncorrect:
            abort(403, message="Incorrect authentication credentials")
        
        return {
            "access_token": token,
            "type": "Bearer",
            "expires_in": lifetime
        }, 201

class UserInfoScopeProvider(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.manager = OAuth2Manager()
        self.security = SecurityManager()
        self.SCB = SecurityCallback
    
    def get(self):
        if not has_token(request.headers):
            abort(401, message="Unauthorized")
        
        token = get_token(request.headers)

        try:
            user = self.manager.get_current_user(token)
        
        except NotAuthenticated:
            abort(401, message="Unauthorized")

        # Converted response model
        response_model = model_to_dict(user)

        # Removed user password for security purposes
        del response_model["password"]

        return response_model, 200
    
    def patch(self):
        if not has_token(request.headers):
            abort(401, message="Unauthorized")
        
        token = get_token(request.headers)

        user = self.manager.update_current_user(token, **request.form)
        
        # Converted response model
        response_model = model_to_dict(user)

        # Removed user password for security purposes
        del response_model["password"]

        return response_model, 201


class AuthenticationLogoutProvider(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.manager = OAuth2Manager()
        self.security = SecurityManager()
        self.SCB = SecurityCallback

    def post(self):
        if not has_token(request.headers):
            abort(401, message="Unauthorized")
        
        # Getting parsed token
        token = get_token(request.headers)

        try:
            self.manager.user_logout(token)
        
        except NotAuthenticated:
            abort(401, "Unauthorized")
        
        return True, 201
