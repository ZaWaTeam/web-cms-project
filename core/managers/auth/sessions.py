from datetime import date
from random import randint

from flask import redirect, make_response, request

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

    def start_session(self, user_id: int, life_time: date, redirect_to: str = "/"):
        """
        Starting session for user.

        return: hashed session token
        """
        user = self.db.user_get(user_id)

        if not user:
            raise UserNotExists

        # Generate usertoken
        token = str(randint(2200, 5000) + user_id)

        # Generate hashed session token
        hashed_token = self.hasher.crypt(token)

        # Get user information
        device = request.user_agent
        ip = request.remote_addr

        # Store in database
        save_session = self.db.create(
            user=user_id, device=device, ip=ip, expires=life_time, token=hashed_token)

        # Failed to store in database
        if not save_session:
            return Log("Cannot store session! Exit code: SESSION_STORE_FAILED", 2)

        # Create cookie

        response = make_response(redirect(redirect_to))

        response.set_cookie("auth", hashed_token, expires=life_time)

        # return response
        return response

    def get_session_and_logout(self, token: str, redirect_on_logout: str = "/"):
        """
        ## Session info

        Get detail about session
        If there is not session. Then it will logout user.
        """
        get_session = self.db.get(token)

        if get_session:
            return get_session

        response = make_response(redirect(redirect_on_logout))

        response.set_cookie('auth', '', expires=0)

        return response

    def get_session(self, token: str):
        """
        ## Session info

        Get detail about session
        If there is not session. Then it will return None.
        """
        get_session = self.db.get(token)

        return get_session
