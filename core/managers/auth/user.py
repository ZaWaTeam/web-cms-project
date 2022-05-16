import configparser
from datetime import date, timedelta
from flask import request
from core.managers.auth.sessions import SessionsManager
from core.managers.hash import Hash
from core.database.crud import users
from core.managers.logging import Log
from core.managers.auth.permissions import PermissionsManagement
from core.configparse import config


class UserManagement:
    """
    ## User Manager class

    Important core part function. Which adds user account feature and allows to manage with them
    It will work with permissions manager and group manager.
    """

    def __init__(self) -> None:
        self.password_hash = Hash()
        self.crud = users.UsersCrud()
        self.permission_manager = PermissionsManagement()
        self.session = SessionsManager()

    def create_user(self, username: str, email: str, password: str, group_id: int = None, **kwargs):
        """
        ## Create user account

        User Management function creates new user

        args (required):
            - `username: str`: Username of new user.
            - `email: str`: Email of new user.
            - `password: str`: Password of new user.

        args (Optional):
            - `**kwargs`: More information field.
        """
        if config.has_option("DEVELOPMENT", "HashTime"):
            hash_password = self.password_hash.crypt(password=password,
                                                     complexity=config.getint("DEVELOPMENT", "HashTime"))
        else:
            hash_password = self.password_hash.crypt(password=password)
        create_user = self.crud.user_create(
            username=username,
            email=email,
            password=hash_password,
            group_id=group_id)

        return create_user

    def create_super_user(self, username: str, email: str, password: str, **kwargs):
        """
        ## Create super user
        """
        new_user = self.create_user(
            username=username, email=email, password=password)

        if not new_user:
            Log("Failed to create new super user", 2)
            return None

        # Get new created user
        get_new_user = self.crud.user_verify(username)

        # Other code, else condition
        create_permission = self.permission_manager.create_permission(
            "*", user=get_new_user.id)

        if create_permission:
            Log("Successfully created new super user!", 3)
            return new_user

    def authenticate_user(self, required_field: str, password: str):
        """
        Authenticate user
        """
        # Verification step 01
        verify_user = self.crud.user_verify(required_field)

        if not verify_user:
            return False

        # Verification step 02
        verify_password = self.password_hash.check(
            password, verify_user.password)

        if not verify_password:
            return False

        # Authentication step 03
        authenticate = self.session.start_session(
            verify_user.id, date.today() + timedelta(weeks=5))

        return authenticate

    def is_authenticated(self, req: request):
        """
        If user is authenticated
        """
        user_account = req.cookies.get("auth")

        if not user_account:
            return None

        get_session = self.session.get_session(user_account)

        return get_session

    def session_checkup(self, req: request):
        """
        If user is authenticated
        """
        user_account = req.cookies.get("auth")

        get_session = self.session.no_session_logout(user_account)

        return get_session

    def get_current_user(self, req: request):
        """
        Gets data about current user
        """
        user = self.is_authenticated(req)

        if user:
            return user.user

        return None

    """
    Other users
    """

    def get_user_info(self, user_id: int):
        """
        Get information about user

        return: True / False
        """
        get_user = self.crud.user_get(id=user_id)

        return get_user

    def users_group_exists(self, user_id: int):
        """
        If user has group it returns True.
        Else False

        return: True / False
        """
        get_user = self.get_user_info(user_id)

        if not get_user:
            return False
            # TODO: Нужно сделать вместо return False. Raise exception

        return get_user.group_id
