class UserManagement:
    """
    ##User Manager class

    Important core part function. Which adds user account feature and allows to manage with them
    It will work with permissions manager and group manager.
    """

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
        pass

    def create_super_user(self, username: str, email: str, password: str, **kwargs):
        """
        ## Create super user
        """
        pass

    def authorize_user(self, required_field: str, password: str):
        """
        Authenticate user
        """
        pass

    def is_authenticated(self):
        """
        If user is authenticated
        """
        pass
