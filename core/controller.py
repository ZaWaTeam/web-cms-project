"""
Web CMS's core controller

This is important file, and if you know what you doing. You can change something here.
But it's too dangerous.
"""
from collections import namedtuple
import json
from core.managers.exceptions import CoreHasDamage
from defines import BASE_DIR


class Controller:
    """
    ### Core main controller. 
    All information, versions, Web CMS API request and input datas starts from here
    """

    def __init__(self) -> None:
        pass

    def core_information(self):
        """
        Information from `core/core.json`
        """
        information = open(f"{BASE_DIR}/core/core.json", "r")

        read = json.load(information)

        information_converted = namedtuple(
            "CoreInformation", read.keys())(*read.values())

        return information_converted

    def core_permissions(self):
        """
        Core permissions.

        returns `Object ("permissions_ident", "permission_description")`
        """

        info = self.core_information()

        if not info.permissions:
            raise CoreHasDamage("Core manifest. Permissions not found!")

        return info.permissions
