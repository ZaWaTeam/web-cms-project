class StorageManager:
    def __init__(self, name: str, store) -> None:
        self.store = store
        self.name = name
    
    def is_current(self, __name: str):
        """
        This method used in Storage Loader as additional check
        """
        return __name == self.name
    
    def save(self):
        self.store.commit(self)