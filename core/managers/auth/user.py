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
        The create_user function creates a new user account.

        :param self: Access variables that belongs to the class
        :param username:str: Specify the username of the user
        :param email:str: Specify the email of the user
        :param password:str: Store the password of the new user
        :param group_id:int=None: Specify a group id for the user
        :param **kwargs: Allow for an arbitrary number of keyword arguments to be passed in
        :return: The result of the crud
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
        The create_super_user function creates a new super user.


        :param self: Reference the class in which the function is defined
        :param username:str: Specify the username of the new user
        :param email:str: Specify the email address of the user
        :param password:str: Set the password of the user
        :param **kwargs: Pass in any additional keyword arguments (hence the name) to our function
        :return: A user object
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

    def authenticate_user(self, required_field: str, password: str, response_on_auth: str):
        """
        The authenticate_user function takes in a required_field and password.
        It then verifies that the user exists, and if so, checks to see if the password matches.
        If both of these are true, it returns True.

        :param self: Reference the class itself
        :param required_field:str: Store the user's email or username
        :param password:str: Store the password entered by the user
        :return: True if the user is successfully authenticated
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
            verify_user.id, date.today() + timedelta(weeks=5), response_on_auth)

        return authenticate

    def is_authenticated(self, req: request):
        """
        The is_authenticated function is used to check if a user is authenticated.
        It takes in the request object and returns either None or the user's account name.

        :param self: Access the class attributes
        :param req:request: Get the request object from flask
        :return: The user_account if the cookie is valid
        """
        user_account = req.cookies.get("auth")

        if not user_account:
            return None

        get_session = self.session.get_session(user_account)

        return get_session

    def session_checkup(self, req: request):
        """
        The session_checkup function is a helper function that is used to check if the user has an active session.
        If they do not, it will redirect them to the login page. If they do have an active session, it will return True.

        :param self: Access attributes and methods of the class in python
        :param req:request: Get the user account from the cookie
        :return: The value of the get_session variable
        """
        user_account = req.cookies.get("auth")

        if not user_account:
            return

        get_session = self.session.no_session_logout(user_account)

        return get_session

    def get_current_user(self, req: request):
        """
        The get_current_user function is a helper function that is used to determine the current user.
        It first checks if the user is authenticated, and then returns either None or the current user.

        :param self: Access the class attributes
        :param req:request: Get the current user's information
        :return: The user object when the user is authenticated
        """
        user = self.is_authenticated(req)

        if user:
            return user.user

        return None

    """
    Other users
    """

    def get_user_info(self, user_id: int) -> bool:
        """
        The get_user_info function accepts a user_id as an argument and returns the corresponding User object.
        If no such User exists, it returns False.

        :param self: Access the class attributes and methods
        :param user_id:int: Get the user_id from the database
        :return: A boolean value
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
