from typing import Union
from ..models.main import *
from . import users


class SessionsCRUD(users.UsersCrud):
    """
    Session Database Operations
    """

    @classmethod
    def create(cls, **kwargs):
        """
        Creates cookie session if it does not exist

        :param cls: Pass the class to create a new instance of
        :param **kwargs: Cookie data
        :return: A tuple of the created object and a boolean value indicating if it was created or not
        """
        # TODO: fix doc
        query = Sessions.get_or_create(**kwargs)

        return query

    @classmethod
    def get(cls, token: str) -> Union[Sessions, None]:
        """
        The get function is a class method that takes in a token and returns the session object
        if it exists. If not, it returns None.

        :param cls: Refer to the current instance of the class in which the method is used
        :param token:str: Get the token from the user
        :return: Session object
        """
        query = Sessions.select().join(UserModel).where(
            Sessions.token == token).get_or_none()

        return query

    @classmethod
    def exists(cls, token: str) -> Union[Sessions, None]:
        """
        The function checks for session existing. If session not exists, it returns none.

        :param cls: Refer to the current instance of the class in which the method is used
        :param token:str: Get the token from the user
        :return: Session object
        """
        query = Sessions.get_or_none(Sessions.token == token)

        return query

    @classmethod
    def delete(cls, token: str) -> None:
        """
        The function checks if session exists, if exists it will delete it from db

        :param cls: Refer to the current instance of the class in which the method is used
        :param token:str: Get the token from the user
        :return: Void, there is nothing to return. In python, void is None
        """
        exists = cls.exists(token)
        if not exists:
            return
        
        Sessions.delete_by_id(exists.id)
        return