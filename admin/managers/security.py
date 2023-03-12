from typing import Callable, Union

from core.managers.auth import permissions, groups
from core.managers.auth.oauth import OAuth2Manager

class SecurityCallback:
    def __init__(self, function: Callable, *args, **kwargs) -> None:
        self.function = function
        self.arguments = args
        self.kwarguments = kwargs
    
    def call(self):
        return self.function(*self.arguments, **self.kwarguments)
    
    def func_bound(self):
        return self.function

class SecurityManager:
    """
    ## Security Manager

    This manager is works with security of control panel.
    Permission control and other happens here.
    Call it where you need.
    This manager containes so much tools to work with security in callin just 1 method.
    """
    # user_manager = user.UserManagement()
    oauth2_manager = OAuth2Manager()
    permission_manager = permissions.PermissionsManagement()
    permission_handler = permissions.PermissionsControllerManager()
    group_manager = groups.GroupsManager()


    def user_authenticated(self, token: str):
        """
        ## If user authenticated

        This method checks is user authenticated or not

        Returns:
            bool: Boolean (True, False). Returns if user authenticated or not.
        """
        user_info = self.oauth2_manager.is_authenticated(token)

        return user_info

    def permission_or_respond(self, token: str, permission: Union[str, list], respond: SecurityCallback, callback: str):
        """
        ## User has permission or else. It will respond from respond argument

        If user have permissions, method will call `callback`.
        If user don't have one of them or permission if it set to 1.
        The `respond` argument will be executed instead if `callback`

        Args:
            permission (Union[str, list]): Permission. It can be 1, only one string. Or multiple,
            if user don't have 1 of them. It will not let him go

            redirect_to (str): Url pattern where user will be redirected if user don't have access.

            callback: function or class which will be executed if user has permissions.

        Returns:
            bool(True): If user has access. 
            redirect(str): If user has not access.
        """
        if not self.user_authenticated(token):
            return respond.call()

        if type(permission) == list:
            perm_check = self.permission_handler.has_permission(
                self.oauth2_manager.get_current_user(token).id, permission)
            if not perm_check:
                return respond.call()

            return callback

        perm_check = self.permission_manager.check_permission(
            permission, self.oauth2_manager.get_current_user(token).id)

        if not perm_check:
            return respond.call()

        return callback

    def logged_or_respond(self, token: str, respond_execute: SecurityCallback, callback: str):
        """
        ## User authenticated, or else execute `respond_execute`

        If user is authenticated. Method will execute argument `callback`
        If user not authenticated. Method will execute `respond_execute` him to url which you will set in argument `respond_execute`
        This method controlls authenticated user or not. And triggers 1 argument of 2 given

        Args:
            respond_execute (SecurityCallback): If user is not authenticated, method will call passed callback function
            callback (SecurityCallback): You can pass here flask response methods. This argument will be executed if user is authenticated in system
        """

        account = self.user_authenticated(token)
        
        if account:
            return callback
        
        return respond_execute.call()
