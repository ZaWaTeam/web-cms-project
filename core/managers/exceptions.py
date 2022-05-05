class ConfigurationNotExistsError(Exception):
    def __init__(self, *args: object, **kwargs) -> None:
        super().__init__(*args)


class ConfigurationAlreadyExistsError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class LogTypeValueError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
