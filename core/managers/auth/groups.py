from core.database.models.main import Groups


class GroupsManager:
    """
    ## Group Management.
    Core function adds accessbillity to groups
    Manage with groups and manager users to add to this group
    """

    @classmethod
    def create_group(self, name: str):
        """
        Create new group.
        """
        query = Groups.create(name=name)
        return query

    @classmethod
    def delete_group(self, group_id: int):
        Groups.delete_by_id(group_id)
        return True

    def edit_group(self, group_id: int, permissions: list[str]):
        pass

    def add_to_group(self, user_id: int, group_id: int):
        pass

    def set_name(self, group_id: int, name: str):
        g = Groups.select().where(Groups.id == group_id).get_or_none()

        if not g:
            return False

        g.name = name
        g.save()
        return True

    def get_group(self, group_id: int):
        query = Groups.select().where(Groups.id == group_id).get_or_none()

        return query
