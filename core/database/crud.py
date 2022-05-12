from core.database.models.main import Editables, Groups, Permissions, UserModel
from core.managers.exceptions import PermissionFollowIndexException
from core.managers.logging import Log
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
        def user_create(cls, username: str, email: str, password: str, group_id: int = None):
            """
            Create & write user to database
            """

            query = UserModel.create(
                username=username, email=email, password=password, group_id=group_id)

            return query

        @classmethod
        def user_get(cls, id: str):
            """
            Gets user by username
            """
            query = UserModel.get_or_none(UserModel.id == id)

            return query

        @classmethod
        def user_get_permission(cls, user_id: int, permission: str):
            """
            Get users permission
            """

            query = Permissions.get_or_none(
                Permissions.permission == permission and Permissions.user_id == user_id)

            return query

        """
        Groups
        """

        @classmethod
        def group_get(cls, group_id: int):
            """
            Gets group by name or create
            """
            query = Groups.get_or_none(Groups.id == group_id)

            return query

        """
        Permissions
        """

        @classmethod
        def create_permission(cls, permission: str, group_id: str = None, user_id: str = None):
            """
            Creates permission
            """
            if group_id is None and user_id is None:
                raise PermissionFollowIndexException(permission)

            elif group_id == None:
                # Define it to user
                query = Permissions.get_or_create(
                    permission=permission, user_id=user_id)

                return query

            elif user_id is None:
                # Define it to group
                query = Permissions.get_or_create(
                    permission=permission, group_id=group_id)

                return query

            return None

        @classmethod
        def user_has_permission(cls, permission: str, user_id: int):
            """
            If user has permissions.

            return bool(True / False)
            """
            query = Permissions.get_or_none(
                (Permissions.user_id == user_id) & (Permissions.permission == permission))

            return query

        @classmethod
        def group_has_permission(cls, permission: str, group_id: int):
            """
            If user has permissions.

            return bool(True / False)
            """
            query = Permissions.select().where((Permissions.group_id ==
                                               group_id) & (Permissions.permission == permission)).get_or_none()

            return query

    class Editables():
        """
        Editables operation
        """

        def create(name: str, value, index: int):
            """
            Create editable
            """

            if 0 < index < 3:
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

            query = Editables.get_or_none(Editables.name == name)

            if not query:
                return False
                # TODO: Raise an exception, ident: edit_not_found

            query.value = value
            query.index = index

            query.save()

            return query
