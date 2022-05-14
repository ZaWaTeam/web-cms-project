from ..models.main import *
from . import users


class SessionsCRUD(users.UsersCrud):
    """
    Session Database Operations
    """

    @classmethod
    def create(cls, **kwargs):
        """
        CRUD create session
        """
        query = Sessions.get_or_create(**kwargs)

        return query

    @classmethod
    def get(cls, token: str):
        """
        CRUD get session from database
        """
        query = Sessions.select().join(UserModel).where(
            Sessions.token == token).get_or_none()

        return query
