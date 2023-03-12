class ConfigurationNotExistsError(Exception):
    def __init__(self, *args: object) -> None:
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


class PermissionNotDefinedInSystem(Exception):
    def __init__(self, permission: str) -> None:
        self.permission = permission

    def __str__(self) -> str:
        return f"Failed to define permission {self.permission}. Are you sure that this is registered permission?"


class PermissionIsAlreadyExistsInDatabase(Exception):
    def __init__(self, permission: str, username: str) -> None:
        self.permission = permission
        self.username = username

    def __str__(self) -> str:
        return f"User {self.username} already has permission \"{self.permission}\" in database!"


class UserNotExists(Exception):
    def __str__(self) -> str:
        return f"User not found!"
    
class UserCredsIncorrect(Exception):
    def __str__(self) -> str:
        return f"User authentication credentials are/is incorrect"

class NotAuthenticated(Exception):
    def __str__(self) -> str:
        return f"User is not authenticated"


class CoreHasDamage(Exception):
    def __init__(self, damage: str) -> None:
        self.damage = damage

    def __str__(self) -> str:
        return f"Web Cms core had damages and errors! {self.damage}"
