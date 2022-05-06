from core.configreader import DataBaseConfig
from core.application import app
from flask import request
from core.managers.logging import Log

"""
Initialized plugin. This functionality file will work with them only
"""
store_config = DataBaseConfig()


"""
* ========== *
  Decorators
* ========== *
"""


class Decorators():
    def user_is_authorized(func):
        # Decorator for authorized user
        # When it will be callen, decorator passes new arguments

        # Arguments: user
        # Argment contains information about user
        def inner():

            @app.before_request
            def request_offered():
                # Starting inner
                # if request.cookies.get("auth"):
                func(user="some_user_info", request=request)

        return inner()


def template_page_loaded(self):
    return True


def admin_page_loaded(self):
    return True


"""
Classes
"""


# Debug logger
class Debug():
    """
    Display and save log.
    -------------------

    Available types:
        - `Debug.log(output (string))`: Info log. Prefix `[info]: log`
        - `Debug.warning(output (string))`: Warning log. Prefix `[warning]: log`. Colors `Yellow`
        - `Debug.error(output (string))`: Error log. Prefix `[error]: log`. Colors `Red`
        - `Debug.success(output (string))`: Success log. Prefix `[success]: log`. Colors `Lime`
    """
    def log(output: str):
        return Log(output, 0)

    def warning(output: str):
        return Log(output, 1)

    def error(output: str):
        return Log(output, 2)

    def success(output: str):
        return Log(output, 3)


# Editables
class Editables():
    def create_editable(name, value, index):
        pass

    def edit_editable(name, value, index):
        pass

    def delete_editable(name):
        pass

    def get_editable(name):
        pass


# File manager
class FileManager():
    def create_file(path: str, name: str, extention: str, content):
        pass

    def write_file(path: str, content, new_name: str = None):
        pass

    def delete_file(path: str):
        pass

    def create_dir(path: str, dirname: str):
        pass

    def edit_dir_name(path: str, new_dirname: str):
        pass

    def delete_dir(path: str):
        pass

# Service


class Service():
    def die(exception):
        pass
