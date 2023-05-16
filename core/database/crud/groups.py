from ..models.main import *


class GroupsCrud:
    """
    Database Operations with Groups.

    Made for managers
    """

    @classmethod
    def create(cls, name: str):
        """
        The create function creates a new group object and adds it to the database.
        It takes in a name as an argument, and returns the newly created Group object.

        :param cls: Refer to the class itself
        :param name:str: Specify the name of the group
        :return: New group object
        """
        query = Groups.create(name=name)
        return query

    @classmethod
    def delete(cls, id: int):
        """
        The delete function will delete a group from the database.



        :param cls: Refer to the class itself
        :param id:int: Specify the id of the group that is to be deleted
        :return: bool success of operation
        """
        query = Groups.delete_by_id(id)
        return query

    @classmethod
    def get_groups(cls):
        """
        The Get Groups function will get all available groups from the database.


        :param cls: Refer to the class itself
        :return: List[Groups] success of operation
        """
        query = Groups.select()
        return query

    @classmethod
    def edit_name(cls, new_name: str, group_id: int):
        """
        This function changes the name of group to new_name

        :param cls: Refer to the class itself, rather than an instance of the class
        :param new_name:str: Set the name of the group
        :param group_id:int: Identify the group that we want to change name of
        :return: bool success of operation
        """
        g = Groups.select().where(Groups.id == group_id).get_or_none()

        if not g:
            return False

        g.name = new_name
        g.save()
        return True

    @classmethod
    def get_group(cls, group_id: int):
        """
        The get_group function takes in a group_id and returns the Group object with that id. If no such group exists, it returns None.

        :param cls: Refer to the class itself, rather than an instance of the class
        :param group_id:int: Get the group id from the database
        :return: A group object
        :doc-author: Trelent
        """
        query = Groups.select().where(Groups.id == group_id).get_or_none()

        return query
