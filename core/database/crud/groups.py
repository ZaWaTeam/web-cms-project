from ..models.main import *


class GroupsCrud():
    """
    Database Operations with Groups.

    Made for managers
    """
    @classmethod
    def create(cls, name: str):
        query = Groups.create(name=name)
        return query

    @classmethod
    def delete(cls, id: int):
        Groups.delete_by_id(id)
        return True

    @classmethod
    def edit_name(cls, new_name: str, group_id: int):
        g = Groups.select().where(Groups.id == group_id).get_or_none()

        if not g:
            return False

        g.name = new_name
        g.save()
        return True

    @classmethod
    def get_group(cls, group_id: int):
        query = Groups.select().where(Groups.id == group_id).get_or_none()

        return query
