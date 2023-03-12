from datetime import datetime, timedelta
from core.database.crud.users import UsersCrud
from core.configparse import config

from core.managers.auth.sessions import SessionsManager
from core.managers.exceptions import NotAuthenticated, UserCredsIncorrect, UserNotExists
from core.managers.hash import Hash
from core.managers.logging import Log

import jwt

class OAuth2Manager:
    def __init__(self) -> None:
        """
        ## OAuth2Manager

        This manager is responsible for managin OAuth authorization process.
        Made for REST API purposes
        """
        self.sessions = SessionsManager()
        self.crud = UsersCrud()
        self.password_hash = Hash()
    
    def authenticate(self, username: str, password: str):
        """
        ## Authenticate

        Authenticates user to system using auth credentials.
        It returns JWT Encoded token which will be used in HTTP-Header requests to allow user access

        Args:
            username (str): Username of existing user
            password (str): Password of existing user
        """
        try:
            # Step 01
            verify_user = self.crud.user_verify(username)

            if not verify_user:
                raise UserNotExists()
            
            # Step 02
            verify_password = self.password_hash.check(password, verify_user.password)
            
            if not verify_password:
                raise UserCredsIncorrect()
            
            # Step 03
            hash_token, life_time = self.sessions.create_session(verify_user.id, datetime.now() + timedelta(weeks=5))

            jwt_token = jwt.encode(payload={"session_token": hash_token.decode('utf-8'), "life_time": str(life_time)}, key=config.get("DEVELOPMENT", "Secret"), algorithm="HS256")

            return jwt_token, str(life_time)
        
        except Exception as e:
            errorname = e.__class__.__name__
            Log(f"`core.managers.auth.oauth`: authenticate method of OAuth2Manager class malfunction. [italic]Error code[italic]: [underline]AUTHENTICATE_ERROR:{errorname}[/underline]", 2)
            if config.get("DEVELOPMENT", "Debug"):
                raise e
            
            return False
    
    def is_authenticated(self, token: str):
        """
        ## Is Authenticated

        The method is_authenticated will check if user is authenticated using JWT-Token

        Args:
            token (str): JWT Token which will be used to get user session
        """
        try:
            jwt_decoded = self.__decode_jwt(token)
            
            if not jwt_decoded:
                return False
            
            session = self.sessions.get_session(jwt_decoded["session_token"])
            
            if not session:
                return False
            
            if session.expires < datetime.now().date():
                print("Closing")
                self.sessions.close_session(jwt_decoded["session_token"])
                return False
            
            return True
        
        except Exception as e:
            errorname = e.__class__.__name__
            Log(f"`core.managers.auth.oauth`: is_authenticated method of OAuth2Manager class malfunction. [italic]Error code[italic]: [underline]AUTHENTICATION_CHECK_ERROR:{errorname}[/underline]", 2)
            if config.get("DEVELOPMENT", "Debug"):
                raise e
            
            return False


    def get_current_user(self, token: str):
        """
        ## Get current user

        Gets information about current user which made request
        The only thing you need to pass in arguments is the token, which you can get from Authorization HTTP Header

        Args:
            token (str): Authentication JWT Token
        """
        if not self.is_authenticated(token):
            raise NotAuthenticated()
        
        jwt_decoded = self.__decode_jwt(token)
        session = self.sessions.get_session(jwt_decoded["session_token"])

        user = self.crud.user_get(session.user_id)

        return user
    
    def update_current_user(self, token: str, **updArgs):
        """
        ## Update current user

        Updates information about current user which made request
        The only thing you need to pass in arguments is the token, which you can get from Authorization HTTP Header

        Args:
            token (str): Authentication JWT Token
        """
        if not self.is_authenticated(token):
            raise NotAuthenticated()
        
        arguments = ["username", "email"]
        
        jwt_decoded = self.__decode_jwt(token)
        session = self.sessions.get_session(jwt_decoded["session_token"])

        user = self.crud.user_get(session.user_id)

        for key, value in updArgs.items():
            if (key in arguments) and hasattr(user, key):
                setattr(user, key, value)

        user.save()

        return user
    
    def user_logout(self, token: str):
        """
        ## User logout

        This method is deletes user session and logs him out

        Args:
            token (str): Authentication JWT Token

        Returns:
            bool: true if operation success, false if operation failed
        
        Raises:
            NotAuthenticated: If provided session token is not exist
        """
        if not self.is_authenticated(token):
            raise NotAuthenticated()
        
        try:
            jwt_decoded = self.__decode_jwt(token)
            self.sessions.close_session(jwt_decoded["session_token"])
        except Exception as e:
            errorname = e.__class__.__name__
            Log(f"`core.managers.auth.oauth`: user_logout method of OAuth2Manager class malfunction. [italic]Error code[italic]: [underline]USER_LOGOUT_ERROR:{errorname}[/underline]", 2)
            if config.get("DEVELOPMENT", "Debug"):
                raise e
            
            return False
        
        return True
    
    
    ###################
    # Private methods #
    ###################
    def __decode_jwt(self, token: str):
        """
        ### [Private] Decode JWT

        Decodes JWT and gets it's content
        Content has to be `session_token` and `life_time`

        Args:
            token (str): Encoded JWT token
        """
        # Decoding encoded JWT token
        try:
            jwt_decoded: dict = jwt.decode(token, key=config.get("DEVELOPMENT", "Secret"), algorithms=["HS256"])
        except:
            # Checking if jwt has "session_token" attribute
            return False
        
        # Check if session token is available
        if jwt_decoded.get("session_token", None) is None:
            return False
        
        return jwt_decoded