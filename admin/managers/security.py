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
    def permission_or_redirect(cls, permission: Union[str, list], redirect_to: str, will_be_exectued):
        """
        ## User has permission or redirect

        If user have permissions, method will call `will_be_executed`.
        If user don't have one of them or permission if it set to 1.
        It will not let him go to control panel

        Args:
            permission (Union[str, list]): Permission. It can be 1, only one string. Or multiple,
            if user don't have 1 of them. It will not let him go

            redirect_to (str): Url pattern where user will be redirected if user don't have access.

            will_be_executed: function or class which will be executed if user has permissions.

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

            return will_be_exectued

        perm_check = cls.permission_manager.check_permission(
            permission, cls.user_manager.get_current_user(request).id)

        if not perm_check:
            return redirect(redirect_to)

        return will_be_exectued

    @classmethod
    def permission_or_respond(cls, permission: Union[str, list], respond, will_be_exectued):
        """
        ## User has permission or else. It will respond from respond argument

        If user have permissions, method will call `will_be_executed`.
        If user don't have one of them or permission if it set to 1.
        The `respond` argument will be executed instead if `will_be_executed`

        Args:
            permission (Union[str, list]): Permission. It can be 1, only one string. Or multiple,
            if user don't have 1 of them. It will not let him go

            redirect_to (str): Url pattern where user will be redirected if user don't have access.

            will_be_executed: function or class which will be executed if user has permissions.

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

            return will_be_exectued

        perm_check = cls.permission_manager.check_permission(
            permission, cls.user_manager.get_current_user(request).id)

        if not perm_check:
            return respond

        return will_be_exectued

    @classmethod
    def logged_or_redirect(cls, redirect_url: str, will_be_executed):
        """
        ## User authenticated, or else redirect

        If user is authenticated. Method will execute argument `will_be_executed`
        If user not authenticated. Method will redirect him to url which you will set in argument `redirect_url`
        This method controlls authenticated user or not. And triggers 1 argument of 2 given

        Args:
            redirect_url (str): If user is not authenticated, method will redirect him to url passed in this argument
            will_be_executed (any): You can pass here flask response methods. This argument will be executed if user is authenticated in system

        Returns:
            redirect_url (str): If user is not authenticated
            will_be_executed (any): If user is authenticated in system
        """

        account = cls.user_authenticated()

        if account:
            return redirect(redirect_url)

        return will_be_executed

    @classmethod
    def logged_or_respond(cls, respond_execute, will_be_executed):
        """
        ## User authenticated, or else execute `respond_execute`

        If user is authenticated. Method will execute argument `will_be_executed`
        If user not authenticated. Method will execute `respond_execute` him to url which you will set in argument `respond_execute`
        This method controlls authenticated user or not. And triggers 1 argument of 2 given

        Args:
            respond_execute (str): If user is not authenticated, method will redirect him to url passed in this argument
            will_be_executed (any): You can pass here flask response methods. This argument will be executed if user is authenticated in system

        Returns:
            respond_execute (str): If user is not authenticated
            will_be_executed (any): If user is authenticated in system
        """

        account = cls.user_authenticated()

        if account:
            return respond_execute

        return will_be_executed
