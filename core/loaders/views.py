class Views():
    def __init__(self) -> None:
        pass

    def load_routers(self, *args):
        """
        load_routers(**args)

        loads given router from /core/mvc/routes/

        """
        for arg in args:
            __import__(f"core.mvc.routes.{arg}", globals(), locals(), [
                       "core", "mvc", "routes"])
