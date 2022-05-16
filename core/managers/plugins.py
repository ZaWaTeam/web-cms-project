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
        # Log(sys.modules[self.__module__].__file__, 0)
        pass

    def on_ready(self):
        pass

    def on_disable(self):
        pass
