from core.database.crud import DatabaseOperations
from core.loaders.permissions import PermissionsLoader
from core.managers.exceptions import PermissionFollowIndexException, PermissionNotDefinedInSystem
from core.managers.logging import Log
from extentions.cli import helpers


class PermissionsManagement():
    """
    ## Permissions management.
    Core function adds accessbillity to permissions
    Manage permissions and check if user has permissions to something or not.
    """

    def __init__(self) -> None:
        self.db = DatabaseOperations

    def create_permission(self, permission: str, group: int = None, user: int = None):
        if group == None and user == None:
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
        create_permission = database.UserCrud.create_permission(
            permission, group, user)

        return create_permission

    def check_for_permission(self, permission: str, user: int = None, group: int = None):
        """
        #### Checking if user or group has permission

        arguments:
            - permission: string - for which you looking for
            - user: string = None - user which have permissions or not
            - group: string = None - group which have permissions or not

        returns: 
            - True: bool - User or Group have permission
            - False: bool - User or Group don't have this perms
        """

        # It can't be group and user both of them are = None
        if not user and not group:
            raise PermissionFollowIndexException(permission)

        if user and group:
            raise PermissionFollowIndexException(permission)

        # If user is set for checking
        if user:

            if self.check_for_superuser(user):
                return True

            # Get details about user
            user_info = self.db.UserCrud.user_get(user)

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

            if self.check_for_superuser(group=group):
                return True

            # Verify that group has permission
            return bool(self.check_group(permission, group))

    def check_for_superuser(self, user: int = None, group: int = None):
        """
        #### Checking if user or group has permission of root user

        arguments:
            - `user: string = None`
            - `group: string = None`

        returns: 
            - `True: bool` - User or Group have permission of root
            - `False: bool` - User or Group don't have permission of root
        """

        if not user and not group:
            raise PermissionFollowIndexException("*")

        if user and group:
            raise PermissionFollowIndexException("*")

        # If user is set
        if user:

            # Get information about user
            user_details = self.db.UserCrud.user_get(user)

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
        ### Check user if it contains permission

        arguments:
            - `permission: string` - What permission are we looking for?
            - `user_id: integer` - What user are we looking for?
        """

        # User variable
        user = self.db.UserCrud.user_get(user_id)

        # User existence condition
        if user:
            verify = self.db.UserCrud.user_has_permission(permission, user_id)

            return verify

        return False

    def check_group(self, permission: str, group_id: int):
        """
        ### Check group if it contains permission

        arguments:
            - `permission: string` - What permission are we looking for?
            - `group_id: integer` - What group are we looking for?
        """

        # User variable
        group = self.db.UserCrud.group_get(group_id)

        # User existence condition
        if group:
            verify = self.db.UserCrud.group_has_permission(
                permission, group_id)

            return verify

        return False
