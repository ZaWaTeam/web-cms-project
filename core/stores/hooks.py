from typing import Callable, List, Literal, Union
from core.managers.storage import StorageManager

class Hook:
    def __init__(self, name: str, type: Literal["action", "filter"], value: Callable) -> None:
        self.name = name
        self.type = type
        self.value = value
    
    def execute(self, *args, **kwargs):
        if self.type == "action":
            return self.value(*args, **kwargs)
        
        elif self.type == "filter":
            return self.value

class HookStore(StorageManager):

    __hooks: List[Hook]

    def __init__(self, name: str, store) -> None:
        super().__init__(name, store)
        self.__hooks = []

    def add_hook(self, hook: Hook):
        hooks = list(map(lambda h: h.name, self.__hooks))

        if hook.name in hooks:
            idx = hooks.index(hook.name)
            self.__hooks[idx] = hook
            return

        self.__hooks.append(hook)
    
    def revoke_hook(self, hook_name: str):
        """
        Revoke hook

        Args:
            hook_name (str): Name of hook which needs to be revoked
        """
        for (idx, hook) in enumerate(self.__hooks):
            if hook.name == hook_name:
                del self.__hooks[idx]
                break
    
    def get_hook(self, hook_name: str):
        """
        Get's specified hook

        Args:
            hook_name (str): The name of the hook
        """
        hooks = list(map(lambda h: h.name, self.__hooks))

        if hook_name in hooks:
            idx = hooks.index(hook_name)
            return self.__hooks[idx]