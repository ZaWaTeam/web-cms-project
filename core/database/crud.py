from core.database.models.main import Editables, Groups, Permissions, UserModel
from core.managers.exceptions import PermissionFollowIndexException
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
                username=username, email=email, password=password, group_id=group_inst.id)

            return query

        @classmethod
        def user_get(cls, username: str):
            """
            Gets user by username
            """
            query = UserModel.get_or_none(UserModel.username == username)

            return query

        @classmethod
        def user_get_permission(cls, username: str, permission: str):
            """
            Get users permission
            """
            user = cls.user_get(username)

            query = Permissions.get_or_none(
                Permissions.permission == permission and Permissions.user_id == user.id)

            return query

        """
        Groups
        """
        @classmethod
        def group_get(cls, group):
            """
            Gets group by name or create
            """
            query = Groups.get_or_none(Groups.name == group)

            return query

        @classmethod
        def group_get_permission(cls, group_name: str, permission: str):
            """
            Get group's permission
            """
            group = cls.group_get(group_name)

            query = Permissions.get_or_none(
                Permissions.group_id == group.id and Permissions.permission == permission)

            return query

        """
        Permissions
        """
        @classmethod
        def create_permission(cls, permission: str, group_name: str = None, user_name: str = None):
            """
            Creates permission
            """
            if group_name == None and user_name == None:
                raise PermissionFollowIndexException(permission)

            elif group_name == None:
                # Define it to user
                user = cls.user_get(user_name)
                query = Permissions.create(
                    permission=permission, user_id=user.id)

                return query

            elif user_name == None:
                # Define it to group
                group = cls.group_get(group_name)
                query = Permissions.create(
                    permission=permission, group_id=group.id)

                return query

            return None

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

            query = Editables.get_or_none(Editables.name == name)

            if not query:
                return False
                # TODO: Raise an exception, ident: edit_not_found

            query.value = value
            query.index = index

            query.save()

            return query
