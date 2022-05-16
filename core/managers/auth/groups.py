from core.database.crud.groups import GroupsCrud


class GroupsManager:
    """
    ## Group Management.
    Core function adds accessibility to groups
    Manage with groups and manager users to add to this group
    """

    @classmethod
    def create_group(cls, name: str):
        """
        The create_group function creates a new group.

        :param name:str: Specify the name of the group
        :return: A new group object
        """
        """
        Create new group.
        """
        return GroupsCrud.create(name)

    @classmethod
    def delete_group(cls, id: int):
        """
        The delete_group function deletes a group from the database.
        It takes one argument, id, which is an integer representing the ID of the group to be deleted.

        :param id:int: Specify the id of the group to be deleted
        :return: success of deletation
        """
        return GroupsCrud.delete(id)

    @classmethod
    def set_name(cls, group_id: int, name: str):
        """
        The set_name function sets the name of a group.

        :param cls: Refer to the class itself
        :param group_id:int: Identify the group
        :param name:str: Name of the group
        :return: new object of edited group
        """
        return GroupsCrud.edit_name(name, group_id)

    @classmethod
    def get_group(cls, group_id: int):
        """
        The get_group function is a class method that takes an integer group_id as its only argument.
        It returns the Group object with that id from the database, or raises a NoResultFound exception if there is no such group.


        :param cls: Refer to the class itself, rather than an instance of the class
        :param group_id:int: Specify the id of the group that is to be returned
        :return: The group object with the given id
        """
        return GroupsCrud.get_group(group_id)
