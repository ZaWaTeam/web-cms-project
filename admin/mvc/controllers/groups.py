from admin.managers.security import SecurityCallback, SecurityManager
from core.managers.auth.groups import GroupsManager
from playhouse.shortcuts import model_to_dict
from flask_restful import Resource


class GroupsProvider(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.security = SecurityManager()
        self.SCB = SecurityCallback

    def get(self):
        groups = GroupsManager.get_groups()

        return list(map(lambda m: model_to_dict(m), groups))

class GroupProvider(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.security = SecurityManager()
        self.SCB = SecurityCallback
    
    def get(self, id: int):
        group = GroupsManager.get_group(id)

        return model_to_dict(group) if group else None
    
