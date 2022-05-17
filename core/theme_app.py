from flask import request
import importlib
from core.managers import editables
from core.configreader import DataBaseConfig
from core.configparse import config
from core.managers.auth.user import UserManagement
from .application import app

config = DataBaseConfig()


class Application():

    title = "Something"
    request = request

    def __init__(self) -> None:
        self.active_template = config.get_config("active_template")
        functionality = importlib.import_module(
            f"content.theme.{self.active_template}.functionality")
        self.__theme_manager = functionality.ThemeFunctionality()

    def get_editable(self, name: str, default: str):
        """
        The get_editable function is a helper function that returns Editable object.


        :param self: Refer to the current instance of the class
        :param name:str: Specify the name of the editable
        :param default:str: Set the default value of the editable
        :return: Editable object or default str if it does not exist
        """
        # Theme manager
        editable_manager = editables.EditableManagers()

        get_editable = editable_manager.get_editable(name)

        if not get_editable:
            return default

        return get_editable

    def load_meta(self):
        """
        The load_meta function loads the static files for a given template.
        It is called in the base.html file and it returns a string of all the static files to be loaded.

        :param self: Access variables that belong to the class
        :return: A html string for style
        """
        # Active template folder name
        active_template = config.get_config("active_template")

        # Template directory
        # dir = f"{BASE_DIR}/content/theme/{active_template}/"

        functionality = importlib.import_module(
            f"content.theme.{active_template}.functionality")

        theme_manager = functionality.ThemeFunctionality()

        static_objects = theme_manager.get_static()

        # Static string
        static_string = ""

        # Src styles
        for static in static_objects["style"]:
            static_string = static_string + \
                f" <link rel=\"stylesheet\" href=\"proj_stat/{static}\">\n"

        # Url styles
        for url in static_objects["url_style"]:
            static_string = static_string + \
                f" <link rel=\"stylesheet\" href=\"{url}\">\n"

        return static_string

    def load_script(self):
        # Active template folder name
        active_template = config.get_config("active_template")

        # Import Template

        functionality = importlib.import_module(
            f"content.theme.{active_template}.functionality")

        theme_manager = functionality.ThemeFunctionality()

        static_objects = theme_manager.get_static()

        # Static string
        static_string = ""

        # Src styles
        for static in static_objects["script"]:
            static_string = static_string + \
                f" <script src=\"proj_stat/{static}\"></script>\n"

        # Url styles
        for url in static_objects["url_script"]:
            static_string = static_string + \
                f" <link rel=\"stylesheet\" href=\"{url}\">\n"

        return static_string

    """
    * ============================== *
      Authentication & Authorization
    * ============================== *
    """

    def user_is_authorized(self):
        # User manager
        user_manager = UserManagement()

        return user_manager.is_authenticated(
            req=request)


app.jinja_env.globals.update(application=Application())
