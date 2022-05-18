from typing import Union

from flask import redirect, request
from core.managers.auth import user, permissions, groups
from core.managers.logging import Log


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
