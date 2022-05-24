from typing import Union

from core.database.models import main as db
from core.managers.exceptions import ConfigurationAlreadyExistsError, ConfigurationNotExistsError
import json


class DataBaseConfig():

    # Create new configuration
    def create_config(self, config_name: str, value: str, exception: bool = False):
        """
        The create_config function creates a new configuration stored in the database.


        :param self: Reference the current instance of the class
        :param config_name:str: Specify the name of the configuration
        :param value:str: Store the value of the configuration
        :param exception:bool=False: Check if the config already exists. If exists, it will raise an exception
        :return: The Configuration object
        """

        if exception:
            self.exists_exception(config_name=config_name, mirror=False)

        query = db.Configuration.create(name=config_name, value=value)

        return query

    # Create configuration with multiple values
    def create_and_parse_config(self, config_name: str, value: Union[list, dict]):
        """
        Create configuration with multiple values
        -----------------------------------------

        Options:
        - config_name: str - Configuration name
        - value: array (dict, list) - Value of configuration
        """

        parsed = json.dumps(value)

        create_conf = self.create_config(config_name, parsed)

        return create_conf

    # Get configuration
    def get_config(self, config_name):
        """
        Get value of configuration
        --------------------------

        Options:
        - config_name: str - Configuration name
        """

        query = db.Configuration.get_or_none(
            db.Configuration.name == config_name)

        if query is None:
            return None

        return query.value

    def get_configs(self, limit: int):
        """
        Get value of configuration
        --------------------------

        Options:
        - config_name: str - Configuration name
        - limit: int - Quantity limit of displaying results
        """

        query = db.Configuration.select().limit(limit)
        return query

    # Get parsed config

    def get_parsed_config(self, config_name):
        """
        Get values of configuration with multiple values
        ------------------------------------------------

        Options:
        - config_name: str - Configuration name
        """

        query = db.Configuration.get_or_none(
            db.Configuration.name == config_name)

        if query is None:
            raise ConfigurationNotExistsError(config_name)

        parse = json.loads(query.value)

        return parse

    def write_config(self, config_name: str, value: str):
        """
        Edit config stored in database
        ------------------------------

        Options:
        - config_name: str - Configuration name
        - value: str - Value of configuration

        """
        self.exists_exception(config_name=config_name, mirror=True)
        query = db.Configuration.get_or_none(
            db.Configuration.name == config_name)

        # Change
        query.value = value
        query.save()

        return query.value

    # Write Parsed Config
    def write_parsed_config(self, config_name: str, value):
        """
        Edit configuration with multiple values
        -----------------------------------------

        Options:
        - config_name: str - Configuration name to change
        - value: array (dict, list) - Value of configuration to change
        """

        parsed = json.dumps(value)

        edit_conf = self.write_config(config_name, parsed)

        return edit_conf

    # Erase configuration
    def erase_config(self, config_name: str):
        """
        Delete configuration stored in database
        ---------------------------------------

        Options:
        - config_name: str - Configuration name to delete
        """
        self.exists_exception(config_name=config_name, mirror=True)

        query = db.Configuration.delete().where(
            db.Configuration.name == config_name)

        query.execute()

        return query

    # Existing
    def is_exists(self, config_name: str):
        query = db.Configuration.get_or_none(
            db.Configuration.name == config_name)

        return bool(query)

    def exists_exception(self, config_name: str, mirror: bool = False):
        query = db.Configuration.get_or_none(
            db.Configuration.name == config_name)

        if not mirror:
            if query is not None:
                raise ConfigurationAlreadyExistsError(config_name)

            return not bool(query)

        if query is None:
            raise ConfigurationNotExistsError(config_name)

        return bool(query)
