from typing import Union

from flask import redirect, request
from core.managers.auth import user, permissions, groups


class SecurityManager:
    """
    ## Security Manager

    This manager is works with security of control panel.
    Permission control and other happens here.
    Call it where you need.
    This manager containes so much tools to work with security in callin just 1 method.
    """
    user_manager = user.UserManagement()
    permission_manager = permissions.PermissionsManagement()
    permission_handler = permissions.PermissionsControllerManager()
    group_manager = groups.GroupsManager()

    @classmethod
    def user_authenticated(cls):
        """
        ## If user authenticated

        This method checks is user authenticated or not

        Returns:
            bool: Boolean (True, False). Returns if user authenticated or not.
        """
        user_info = cls.user_manager.is_authenticated(request)

        return bool(user_info)

    @classmethod
    def permission_or_redirect(cls, permission: Union[str, list], redirect_to: str, callback):
        """
        ## User has permission or redirect

        If user have permissions, method will call `callback`.
        If user don't have one of them or permission if it set to 1.
        It will not let him go to control panel

        Args:
            permission (Union[str, list]): Permission. It can be 1, only one string. Or multiple,
            if user don't have 1 of them. It will not let him go

            redirect_to (str): Url pattern where user will be redirected if user don't have access.

            callback: function or class which will be executed if user has permissions.

        Returns:
            bool(True): If user has access. 
            redirect(str): If user has not access.
        """
        if not cls.user_authenticated():
            return redirect(redirect_to)

        if type(permission) == list:
            perm_check = cls.permission_handler.has_permission(
                cls.user_manager.get_current_user(request).id, permission)
            if not perm_check:
                return redirect(redirect_to)

            return callback

        perm_check = cls.permission_manager.check_permission(
            permission, cls.user_manager.get_current_user(request).id)

        if not perm_check:
            return redirect(redirect_to)

        return callback

    @classmethod
    def permission_or_respond(cls, permission: Union[str, list], respond, callback):
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
        if not cls.user_authenticated():
            return respond

        if type(permission) == list:
            perm_check = cls.permission_handler.has_permission(
                cls.user_manager.get_current_user(request).id, permission)
            if not perm_check:
                return respond

            return callback

        perm_check = cls.permission_manager.check_permission(
            permission, cls.user_manager.get_current_user(request).id)

        if not perm_check:
            return respond

        return callback

    @classmethod
    def logged_or_redirect(cls, redirect_url: str, callback):
        """
        ## User authenticated, or else redirect

        If user is authenticated. Method will execute argument `callback`
        If user not authenticated. Method will redirect him to url which you will set in argument `redirect_url`
        This method controlls authenticated user or not. And triggers 1 argument of 2 given

        Args:
            redirect_url (str): If user is not authenticated, method will redirect him to url passed in this argument
            callback (any): You can pass here flask response methods. This argument will be executed if user is authenticated in system

        Returns:
            redirect_url (str): If user is not authenticated
            callback (any): If user is authenticated in system
        """

        account = cls.user_authenticated()

        if account:
            return redirect(redirect_url)

        return callback

    @classmethod
    def logged_or_respond(cls, respond_execute, callback):
        """
        ## User authenticated, or else execute `respond_execute`

        If user is authenticated. Method will execute argument `callback`
        If user not authenticated. Method will execute `respond_execute` him to url which you will set in argument `respond_execute`
        This method controlls authenticated user or not. And triggers 1 argument of 2 given

        Args:
            respond_execute (str): If user is not authenticated, method will redirect him to url passed in this argument
            callback (any): You can pass here flask response methods. This argument will be executed if user is authenticated in system

        Returns:
            respond_execute (str): If user is not authenticated
            callback (any): If user is authenticated in system
        """

        account = cls.user_authenticated()

        if account:
            return respond_execute

        return callback
