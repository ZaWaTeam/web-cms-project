from typing import List
from core.managers.logging import Log
from core.managers.storage import StorageManager
from flask import Flask


class StorageLoader:
    
    __stores: List[object]

    def __init__(self, app: Flask) -> None:
        self.app = app
        self.__stores = []
    
    @property
    def stores(self):
        return self.__stores
    
    def add(self, name: str, store: StorageManager, *args, **kwargs):
        try:
            store = store(name, self, *args, **kwargs)
            self.__stores.append(store)
        
        except Exception as e:
            Log(f"Failed to load store with identified name [bold]{name}[/bold] store", 2)
            raise e
        
        finally:
            Log(f"Successfuly initialized store [bold]{name}[/bold]", 0)
    
    def dispatch(self, name: str):
        """
        Dispatch is method to call certain store class

        Args:
            name (str): Name of dispatching store
        """
        result = list(filter(lambda c: c.is_current(name), self.__stores))

        if not len(result):
            Log(f"Could not find the store with the specified name [bold]{name}[/bold]")
            return
        
        return result[0]
    
    def commit(self, new_value: object):
        """
        Commit is method to update storage data

        Args:
            new_value (StorageManager): Updated model from dispatch()
        """
        name: str = new_value.name

        for index, item in enumerate(self.__stores):
            if item.is_current(name):
                self.__stores[index] = new_value
                break
        
        return new_value