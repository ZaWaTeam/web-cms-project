from datetime import date
from random import randint

from flask import redirect, make_response, request

from core.configparse import config
from core.database.crud.sessions import SessionsCRUD
from core.managers.exceptions import UserNotExists
from core.managers.hash import Hash
from core.managers.logging import Log


class SessionsManager:
    """
    ## Managing sessions

    This class made for managing user session.
    """
    db = SessionsCRUD()
    hasher = Hash()

    def start_session(self, user_id: int, life_time: date, response: str):
        """
        The start_session function creates a new session for the user.
        It takes in two parameters, user_id and life_time.
        The function returns hashed token.

        :param self: Access variables that belongs to the class
        :param user_id:int: User that starts the session
        :param life_time:date: Set the expiry date of the cookie
        :param redirect_to:str=&quot;/&quot;: Redirect the user to a specific page after they have logged in
        :return: The hashed session token
        """
        user = self.db.user_get(user_id)

        if not user:
            raise UserNotExists

        # Generate usertoken
        token = str(randint(2200, 5000) + user_id)

        # Generate hashed session token
        if config.has_option("DEVELOPMENT", "HashTime"):
            hashed_token = self.hasher.crypt(
                token, complexity=config.getint("DEVELOPMENT", "HashTime"))
        else:
            hashed_token = self.hasher.crypt(token)
        # Get user information
        device = request.user_agent
        ip = request.remote_addr

        # Store in database
        save_session = self.db.create(
            user=user_id, device=device, ip=ip, expires=life_time, token=hashed_token)

        # Failed to store in database
        if not save_session:
            Log("Cannot store session! Exit code: SESSION_STORE_FAILED", 2)
            return False
        # Create cookie

        response = make_response(response)

        response.set_cookie("auth", hashed_token, expires=life_time)

        # return response
        return response

    def no_session_logout(self, token: str, redirect_on_logout: str = "/"):
        """
        The no_session_logout function is used to logout user.
        If there is no session, then it will redirect to login page.

        :param self: Access variables that belongs to the class
        :param token:str: Get the token from the cookie
        :param redirect_on_logout:str=&quot;/&quot;: Redirect the user to a specific page after they have been logged out
        :return: response, if session exists, else None
        """
        get_session = self.db.exists(token=token)

        if get_session:
            return

        response = make_response(redirect(redirect_on_logout))

        response.set_cookie('auth', '', expires=0)

        return response

    def get_session(self, token: str):
        """
        The get_session function retrieves the session object for a given token.
        If there is no session, then it returns None.

        :param self: Access variables that belongs to the class
        :param token:str: Get the session info
        :return: Session object
        """
        get_session = self.db.get(token)

        return get_session
