from core.database.crud import DatabaseOperations
from core.managers.logging import Log


class EditableManagers():

    __database = DatabaseOperations()

    def __init__(self) -> None:
        pass

    def set_editable(self, name: str, value, index: int):
        get_argument = self.__get_argument(name)
        if not get_argument:
            set_argument = self.__set_argument(name, value, index)

            return set_argument

        argument = self.__get_argument(name)

        return argument

    def get_editable(self, name: str):
        get_argument = self.__get_argument(name)

        return get_argument

    def edit_editable(self, name: str, value, index: int):
        edit_argument = self.__edit_argument(name, value, index)

        return edit_argument

    def __set_argument(self, name: str, value, index: int):
        # Database declare
        database = self.__database

        create_crud = database.Editables.create(
            name=name, value=value, index=index)

        print(f"[log]: Creating argument '{name}' - status {create_crud}")

        return create_crud

    def __edit_argument(self, name: str, value, index: int):
        # Database declaration

        database = self.__database

        edit_crud = database.Editables.edit(
            name=name, value=value, index=index)

        return edit_crud

    def __get_argument(self, name: str):
        # Database declaration

        database = self.__database

        operation = database.Editables.get(name)

        return operation
