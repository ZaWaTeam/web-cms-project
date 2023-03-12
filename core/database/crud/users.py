from typing import Union
from core.managers.exceptions import PermissionFollowIndexException
from ..models.main import *


class UsersCrud:
    """
    User CRUD operations
    """

    @classmethod
    def user_create(cls, username: str, email: str, password: str, group_id: int = None):
        """
        The user_create function creates a user in the database.
        It takes four parameters: username, email, password and group_id.
        If no group_id is specified then it will default to None.

        :param cls: Refer to the class itself, rather than an instance of the class
        :param username:str: Specify the username of the user
        :param email:str: Specify the email address of the user
        :param password:str: Store the password in a hashed form
        :param group_id:int=None: Specify a default value for the group_id parameter
        :return: The query object that is returned by the create function
        """

        query = UserModel.create(
            username=username, email=email, password=password, group_id=group_id)

        return query

    @classmethod
    def user_get(cls, id: int):
        """
        The user_get function is used to retrieve a user from the database.
        It takes one argument, id, which is the primary key of the user in question.
        If there is no such user in the database, it returns None.

        :param cls: Refer to the class itself, rather than an instance of the class
        :param id:int: Specify the id of the user we want to get
        :return: The user with the id passed in as a parameter
        """
        query = UserModel.get_or_none(UserModel.id == id)
        
        return query

    @classmethod
    def user_verify(cls, username: str) -> Union[UserModel, None]:
        """
        The user_verify function is a class method that takes in a username and returns the user object if it exists.


        :param cls: Refer to the class itself, rather than an instance of the class
        :param username:str: Get the username from the user
        :return: The user object if the username is found in the database
        """
        query = UserModel.get_or_none(UserModel.username == username)

        return query

    @classmethod
    def get_user_permission(cls, user_id: int, permission: str):
        """
        Checks if user has a permission, if yes, returns it, else None

        :param cls: Refer to the class itself, rather than an instance of the class
        :param user_id:int: Specify the user_id of the user that we want to get permissions for
        :param permission:str: Specify the permission that is being requested
        :return: The permission for the user or None
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
        The group_get function retrieves a group by its id.



        :param cls: Access the class methods
        :param group_id:int: Specify the id of the group that is to be retrieved
        :return: A group object
        """
        query = Groups.get_or_none(Groups.id == group_id)
        return query

    @classmethod
    def add_user_to_group(cls, user_id: int, group_id: int):
        """
        The add_user_to_group function adds a user to a group.
        It takes two arguments, the first is the id of the user and
        the second is the id of the group. It returns True if it was successful and False otherwise.

        :param cls: Refer to the class itself, rather than an instance of the class
        :param user_id:int: Specify the user that is being added to a group
        :param group_id:int: Specify the group that the user will be added to
        :return: bool success - True or fail - False
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
    def create_permission(cls, permission: str, group_id: str = None, user_id: str = None) -> tuple[Permissions, bool]:
        """
        The create_permission function creates a permission for either a user or group.
        It takes in two parameters, the first being the permission and the second being either
        the user_id or group_id of which to create permissions for. If both are None, then an error is raised.
        If only one is None, then it creates that permission to be assigned to another parameter (user/group).
        If both are not none, then it creates that specific permisison for that specific user/group.

        :param cls: Refer to the class itself, so that we can call its functions
        :param permission:str: Define the permission that is going to be created
        :param group_id:str=None: Define the permission to a group
        :param user_id:str=None: Define the permission to a user
        :return: A tuple with the permission object and a boolean value
        """
        """
        Creates permission
        """
        if group_id is None and user_id is None:
            raise PermissionFollowIndexException(permission)

        elif group_id is None:
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
        The user_has_permission function checks if a user has the permission specified by the parameter.
        It does this by checking if there is an entry in the permissions table that matches both
        the user_id and permission parameters. If such an entry exists, then it returns True, otherwise False.

        :param cls: Reference the class that is being called
        :param permission:str: Check if the user has a specific permission
        :param user_id:int: Check if the user has a specific permission
        :return: A boolean value
        """
        query = Permissions.get_or_none(
            (Permissions.user_id == user_id) & (Permissions.permission == permission))

        return query

    @classmethod
    def group_has_permission(cls, permission: str, group_id: int):
        """
        The group_has_permission function is a class method that takes in two arguments, permission and group_id.
        It then queries the database to see if there is a match for the given group_id and permission. If there is, it returns True,
        otherwise it returns False.

        :param cls: Reference the class that is being called
        :param permission:str: Check if the user has that permission
        :param group_id:int: Specify the group_id of the group that you want to check if it has a certain permission
        :return: A boolean value
        """
        query = Permissions.select().where((Permissions.group_id ==
                                            group_id) & (Permissions.permission == permission)).get_or_none()

        return query
