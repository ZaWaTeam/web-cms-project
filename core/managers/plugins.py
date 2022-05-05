import sys
from typing import final

from flask import request
from core.managers.logging import Log
from core.configreader import DataBaseConfig
from core.application import app


class PluginGeneric():
    """
      Plugin Generic \n
      Method overrider
    """

    def __init__(self) -> None:
        Log(sys.modules[self.__module__].__file__, 0)

    # @final
    # def user_is_authorized(self, func):
    #     # Decorator for authorized user
    #     # When it will be callen, decorator passes new arguments

    #     # Arguments: user
    #     # Argment contains information about user
    #     def inner(self):
    #         print("Hello")
    #         call_func = func(user="sadasd")
    #         print("Something")

    #         return call_func

    #         # @app.before_request()
    #         # def request_offered():
    #         #     # Starting inner
    #         #     # if request.cookies.get("auth"):
    #         #     func(user="some_user_info")

    #     return inner()

    def on_ready(self):
        pass

    def on_disable(self):
        pass
