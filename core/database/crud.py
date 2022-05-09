from core.database.models.main import Editables, Groups, UserModel
from .models import *
import json


class DatabaseOperations():
    def __init__(self) -> None:
        pass

    class UserCrud():
        """
        User CRUD operations
        """
        @classmethod
        def user_create(cls, username: str, email: str, password: str, group):
            """
            Create & write user to database
            """
            group_inst = cls.group_get_create(group)

            query = UserModel.create(
                username=username, email=email, password=password, group_id=1)

            return query

        """
        Groups
        """
        @classmethod
        def group_get_or_default(cls, group):
            """
            Gets group by name or create
            """
            query = Groups.get_or_create(name=group)

            return query

    class Editables():
        """
        Editables operation
        """
        def create(name: str, value, index: int):
            """
            Create editable
            """

            if index > 0 and index < 3:
                value = json.dumps(value)

            query = Editables.create(name=name, value=value, index=index)

            return query

        def get(name: str):
            """
            Get editable
            """

            query = Editables.get_or_none(Editables.name == name)

            if query:
                if query.index > 0 and query.index < 3:
                    value = json.loads(query.value)

                    return value

                return query.value

            return None

        def edit(name: str, value, index: int):
            """
            Edit editable
            """

            if index > 0 and index < 3:
                value = json.dumps(value)

            query = Editables.get_or_none(name)

            if not query:
                return False
                # TODO: Raise an exception, ident: edit_not_found

            query.value = value
            query.index = index

            query.save()

            return query
