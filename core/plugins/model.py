import os
import inspect
from core.database.connect import CpDb
from peewee import *


def plugin_table(model_class):
    """
    Make name of plugin table

    Args:
        model_class: Parent model class, which will be passed.
    """
    # Get model name
    model_name = model_class.__name__

    plugin_dir = list(os.path.split(inspect.getfile(model_class)))

    plugin = plugin_dir[1].replace(".py", "")

    # Return model name
    return f'{plugin}_' + model_name.lower()


class PluginModel(Model):

    class Meta:
        database = CpDb
        table_function = plugin_table


class ModelController:
    """
    Model controller contains some methods, to create tables in database

    Use this to interact with database.
    """

    @classmethod
    def create_model_tables(cls, models: list):
        """
        ## Create mode tables

        To create model in tables.
        Method will add to base model variable all models.

        Args:
            models (list): List of model classes.
        """
        CpDb.create_tables(models)
