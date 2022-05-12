from core.database.models.main import Editables, Groups, Permissions, UserModel
from core.managers.exceptions import PermissionFollowIndexException
from core.managers.logging import Log
from ..models import *
import json


class DatabaseOperations():
    def __init__(self) -> None:
        pass

    """
    Editables operation
    """

    def create(self, name: str, value, index: int):
        """
        Create editable
        """

        if 0 < index < 3:
            value = json.dumps(value)

        query = Editables.create(name=name, value=value, index=index)

        return query

    def get(self, name: str):
        """
        Get editable
        """

        query = Editables.get_or_none(Editables.name == name)

        if query:
            if query.index > 0 and query.index < 3:
                value = json.loads(query.value)

                return value

            return query.value

        return None

    def edit(self, name: str, value, index: int):
        """
        Edit editable
        """

        if index > 0 and index < 3:
            value = json.dumps(value)

        query = Editables.get_or_none(Editables.name == name)

        if not query:
            return False
            # TODO: Raise an exception, ident: edit_not_found

        query.value = value
        query.index = index

        query.save()

        return query
