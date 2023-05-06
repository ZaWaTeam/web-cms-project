from core.managers.plugins import PluginGeneric
from core.configreader import DataBaseConfig
from core.managers.logging import Log
from core.theme_app import Application, app

"""
Initialized plugin. This functionality file will work with them only
"""
store_config = DataBaseConfig()


"""
* ========== *
  Decorators
* ========== *
"""


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

class ApplicationManagement():
    """
    Manage theme global variable application.
    --------------------------------------

    Plugin developer can create any type of variable on application
    Also he can manage already existing variables.
    Be careful when using this, you can break CMS.
    """
    application: Application
    def __init__(self, plugin: PluginGeneric) -> None:
        self.plugin = plugin
        self.application = app.jinja_env.globals.get("application", None)
    
    def set_variable(self, name: str, value) -> None:
        """
        Setting external variable.
        Note: We recommend use your plugin prefix in variable name to prevent rewriting system variables

        Args:
            name (str): Name of new variable
            value (any): Value of new variable
        """
        setattr(self.application, name, value)
    
    def get_variable(self, name: str):
        """
        It will get existing variable
        Will return None if there not found

        Args:
            name (str): Name of variable
        """
        variable = getattr(self.application, name, None)

        return variable

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
    def die(self, exception: object):
        pass
