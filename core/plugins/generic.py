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
    @classmethod
    def user_is_authorized(self, func):
        # Decorator for authorized user
        # When it will be callen, decorator passes new arguments

        # Arguments: user
        # Argment contains information about user
        def inner():

            @app.before_request
            def request_offered():
                # Starting inner
                if request.cookies.get("auth"):
                    func(user=request)

        return inner()

    @classmethod
    def on_request(self, func):
        """
        Decorator on request will be callen when site visitor or client makes request to server
        when client enters site. This decorator will be triggered.

        It passes some arguments:
        `request: namedtuple` - request information
        """
        def inner():

            @app.before_request
            def request_offered():
                # Starting request inner
                func(request)

        return inner()


"""
Methods without classes
"""
# Это метод без класса, self не нужно


def template_page_loaded():
    return True


def admin_page_loaded():
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
    @classmethod
    def log(self, output: str):
        return Log(output, 0)

    @classmethod
    def warning(self, output: str):
        return Log(output, 1)

    @classmethod
    def error(self, output: str):
        return Log(output, 2)

    @classmethod
    def success(self, output: str):
        return Log(output, 3)


# Editables
class Editables():
    @classmethod
    def create_editable(self, name, value, index):
        pass

    @classmethod
    def edit_editable(self, name, value, index):
        pass

    @classmethod
    def delete_editable(self, name):
        pass

    @classmethod
    def get_editable(self, name):
        pass


# File manager
class FileManager():
    @classmethod
    def create_file(self, path: str, name: str, extention: str, content):
        pass

    @classmethod
    def write_file(self, path: str, content, new_name: str = None):
        pass

    @classmethod
    def delete_file(self, path: str):
        pass

    @classmethod
    def create_dir(self, path: str, dirname: str):
        pass

    @classmethod
    def edit_dir_name(self, path: str, new_dirname: str):
        pass

    @classmethod
    def delete_dir(self, path: str):
        pass

# Service


class Service():
    @classmethod
    def die(self, exception):
        pass
