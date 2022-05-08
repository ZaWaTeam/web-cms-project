from core.managers.hash import Hash
from core.database.crud import DatabaseOperations


class UserManagement:
    """
    ## User Manager class

    Important core part function. Which adds user account feature and allows to manage with them
    It will work with permissions manager and group manager.
    """

    def __init__(self) -> None:
        self.password_hash = Hash()
        self.crud = DatabaseOperations()

    def create_user(self, username: str, email: str, password: str, **kwargs):
        """
        ## Create user account

        User Management function creates new user

        args (required):
            - `username: str`: Username of new user.
            - `email: str`: Email of new user.
            - `password: str`: Password of new user.

        args (Optional):
            - `**kwargs`: More information field.
        """
        hash_password = self.password_hash.crypt(password=password)
        create_user = self.crud.UserCrud.user_create(
            username=username, email=email, password=hash_password, group="Default")

        return create_user

    @classmethod
    def create_super_user(cls, username: str, email: str, password: str, **kwargs):
        """
        ## Create super user
        """
        pass

    @classmethod
    def authorize_user(cls, required_field: str, password: str):
        """
        Authenticate user
        """
        pass

    @classmethod
    def is_authenticated(cls):
        """
        If user is authenticated
        """
        pass
