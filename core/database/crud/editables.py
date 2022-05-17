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
        The create function creates an editable with the given name and value.
        It also takes in an index to determine which type editable it is creating

        :param self: Access variables that belongs to the class
        :param name:str: Specify the name of the editable
        :param value: Store the value of the editable
        :param index:int: Determine if the editable is a str, list or dict
        :return: Editables object
        """

        if 0 < index < 3:
            value = json.dumps(value)

        query = Editables.create(name=name, value=value, index=index)

        return query

    def get(self, name: str):
        """
        Get Editables object by name

        :param self: Access variables that belongs to the class
        :param name:str: Specify the name of the editable
        :return: Object of Edititables
        """

        query = Editables.get_or_none(Editables.name == name)

        if query:
            if 0 < query.index < 3:
                value = json.loads(query.value)

                return value

            return query.value

        return None

    def edit(self, name: str, value, index: int):
        """
        The edit function is used to edit the value of an editable.
        It takes three arguments: name, value and index.
        The name argument is a string that represents the name of the editable you want to change.
        The value argument is a json object that represents what you want to change it too (see below).
        The index argument is an integer between 0 and 2 inclusive, representing which field in the database you are changing.

        :param self: Access variables that belongs to the class
        :param name:str: Identify the editable
        :param value: Determine what the value of the editable is
        :param index:int: Determine which editable to change
        :return: False if failed, else edited Editable object
        """

        if 0 < index < 3:
            value = json.dumps(value)

        query = Editables.get_or_none(Editables.name == name)

        if not query:
            return False
            # TODO: Raise an exception, ident: edit_not_found

        query.value = value
        query.index = index

        query.save()

        return query
