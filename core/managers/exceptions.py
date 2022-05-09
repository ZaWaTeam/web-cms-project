class ConfigurationNotExistsError(Exception):
    def __init__(self, *args: object, **kwargs) -> None:
        super().__init__(*args)


class ConfigurationAlreadyExistsError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class LogTypeValueError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class PluginManifestError(Exception):
    def __init__(self, plugin_name: str) -> None:
        self.plugin_name = plugin_name

    def __str__(self) -> str:
        return f"PluginManifestError: Plugin {self.plugin_name} doesn't contains 'manifest.json'. If you're developer of this plugin. Check documentation of plugin development"


class PermissionFollowIndexException(Exception):
    def __init__(self, permission: str) -> None:
        self.permission = permission

    def __str__(self) -> str:
        return f"You trying to create permission {self.permission} without indexing it to group or user!"
