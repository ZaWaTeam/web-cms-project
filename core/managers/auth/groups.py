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
        Create new group.
        """
        return GroupsCrud.create(name)

    @classmethod
    def delete_group(cls, id: int):
        """
        Delete a group
        """
        return GroupsCrud.delete(id)

    @classmethod
    def set_name(cls, group_id: int, name: str):
        """
        Set name of group
        """
        return GroupsCrud.edit_name(name, group_id)

    @classmethod
    def get_group(cls, group_id: int):
        """
        Get Group object from db by id
        """
        return GroupsCrud.get_group(group_id)
