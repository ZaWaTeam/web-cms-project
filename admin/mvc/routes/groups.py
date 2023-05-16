from admin.mvc.controllers.groups import GroupsProvider
from core.application import api

api.add_resource(GroupsProvider, "/groups/all")