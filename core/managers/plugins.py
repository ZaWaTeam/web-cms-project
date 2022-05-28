

class PluginGeneric():
    """
      Plugin Generic \n
      Plugin development interface. For building apps
    """

    def __init__(self) -> None:
        # Log(sys.modules[self.__module__].__file__, 0)
        pass

    def on_enable(self):
        pass

    def on_ready(self):
        pass

    def on_request(self, request):
        pass

    def on_fixedrequest(self, request):
        pass

    def on_disable(self):
        pass
