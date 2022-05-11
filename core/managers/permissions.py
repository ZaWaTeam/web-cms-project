from core.database.crud import DatabaseOperations
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
