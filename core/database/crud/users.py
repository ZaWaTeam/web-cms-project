from .groups import GroupsCrud
from ..models.main import *
from core.managers.exceptions import PermissionFollowIndexException


class UsersCrud:
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
    def user_get(cls, id: int):
        """
        Gets user by username
        """
        query = UserModel.get_or_none(UserModel.id == id)

        return query

    @classmethod
    def user_verify(cls, username: str):
        """
        Gets user by username
        """
        query = UserModel.get_or_none(UserModel.username == username)

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

    @classmethod
    def add_user_to_group(cls, user_id: int, group_id: int):
        """
        Add user to group(change group of user)
        """
        user = UserModel.get_or_none(UserModel.id == user_id)
        if not user:
            return False
        user.group = group_id
        user.save()
        return True

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
