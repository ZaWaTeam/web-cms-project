from flask import request
from core.application import app
from core.database.crud import users
from core.loaders.permissions import PermissionsLoader
from core.managers.exceptions import PermissionFollowIndexException, PermissionNotDefinedInSystem
from extentions.cli import helpers


class PermissionsManagement():
    """
    ## Permissions management.
    Core function adds accessbillity to permissions
    Manage permissions and check if user has permissions to something or not.
    """

    def __init__(self) -> None:
        self.db = users.UsersCrud()

    def create_permission(self, permission: str, group: int = None, user: int = None):
        """
        The create_permission function creates a permission in the database.

        :param self: Reference the class instance
        :param permission:str: Define the permission that is going to be created
        :param group:int=None: Define the group of the permission
        :param user:int=None: Define if the permission is assigned to a user or group
        :return: The permission object
        """
        if group is None and user is None:
            raise PermissionFollowIndexException(permission)

        # Database
        database = self.db

        # Loader
        permission_loader = PermissionsLoader()

        find_match = helpers.find_filter(
            "identy", permission, permission_loader.permissions)

        # If there is no registered permission. But user tryes to define it
        if not find_match:
            if permission != "*":
                raise PermissionNotDefinedInSystem(permission)

        # Create permission in database
        create_permission = database.create_permission(
            permission, group, user)

        return create_permission

    def check_permission(self, permission: str, user: int = None, group: int = None):
        """
        The check_permission function is used to check if a user or group has permission.
        It takes three arguments: the permission, the user and the group. If both are None, it will raise an exception.

        :param self: Access variables that belong to the class
        :param permission:str: Check if user or group has permission
        :param user:int=None: Check if the user has a permission or not
        :param group:int=None: Check if the user is in a group or not
        :return: A boolean if group or user has a permission
        """

        # It can't be group and user both of them are = None
        if not user and not group:
            raise PermissionFollowIndexException(permission)

        if user and group:
            raise PermissionFollowIndexException(permission)

        # If user is set for checking
        if user:

            if self.check_superuser(user):
                return True

            # Get details about user
            user_info = self.db.user_get(user)

            # If user not exists
            if not user_info:
                return False

            # If user has group
            if user_info.group_id:

                if self.check_group(permission, user_info.group_id):
                    return bool(self.check_group(permission, user_info.group_id))

            # Or if user has permission
            return bool(self.check_user(permission, user))

        if group:

            if self.check_superuser(group=group):
                return True

            # Verify that group has permission
            return bool(self.check_group(permission, group))

    def check_superuser(self, user: int = None, group: int = None):
        """
        The check_superuser function checks if the user or group has permission(*) of root user.


        :param self: Access variables that belongs to the class
        :param user:int=None: User id
        :param group:int=None: Group id
        :return: True if the user or group has permission of root user
        """

        if not user and not group:
            raise PermissionFollowIndexException("*")

        if user and group:
            raise PermissionFollowIndexException("*")

        # If user is set
        if user:

            # Get information about user
            user_details = self.db.user_get(user)

            if not user_details:
                return False

            if user_details.group_id:
                # Define group checker

                group_check = self.check_group("*", user_details.group_id)

                # If group which current user implements exists.
                if group_check:
                    return bool(group_check)

            return bool(self.check_user("*", user))

        if group:
            return bool(self.check_group("*", group))

    def check_user(self, permission: str, user_id: int):
        """
        The check_user function checks if a user has a certain permission.


        :param self: Access variables that belongs to the class
        :param permission:str: Tell the function what permission we are looking for
        :param user_id:int: Get the user from the database
        :return: A boolean value that shows if user has permission
        """

        # User variable
        user = self.db.user_get(user_id)

        # User existence condition
        if user:
            verify = self.db.user_has_permission(permission, user_id)

            return verify

        return False

    def check_group(self, permission: str, group_id: int):
        """
        The check_group function checks if a group has a permission.

        :param self: Access variables that belongs to the class
        :param permission:str: Permission name
        :param group_id:int: Specify the group to check
        :return: A boolean value that shows if group has permission
        """

        # User variable
        group = self.db.group_get(group_id)

        # User existence condition
        if group:
            verify = self.db.group_has_permission(
                permission, group_id)

            return verify

        return False


class PermissionsControllerManager():
    db = users.UsersCrud()
    permissions_loader = PermissionsLoader()
    permissions_manager = PermissionsManagement()

    @classmethod
    def get_available_permissions(cls):
        """
        The get_available_permissions function returns a list of all the permissions in the system.
        The permissions are returned as a dictionary with two keys: 'permissions' and 'groups'.
        The value for each of these keys is a list of dictionaries, where each dictionary contains
        the name, description, and id number for that permission or group. The id numbers can be used to
        associate groups with individual users.

        :param cls: Access variables that belongs to the class
        :return: all existing permissions
        """
        permissions_in_system = cls.permissions_loader.permissions

        return permissions_in_system

    """
    * =============== *
      Request Handler
    * =============== *
    """

    @classmethod
    def has_permission(cls, user_id: int, permissions: list = None):
        """
        The has_permission function is a helper function that checks if the user has ALL permissions from list

        :param cls: Refer to the class itself, rather than an instance of the class
        :param user_id:int: User id to check
        :param permissions:list=None: Pass a list of permissions that the user must have
        :return: True if user has ALL permissions from list that was passed, else False
        """
        if permissions is None:
            permissions = []

        if not bool(len(permissions)):
            return False

        for permission in permissions:
            permission_check = cls.permissions_manager.check_permission(
                permission=permission, user=user_id, group=None)

            if not permission_check:
                return False

        return True
