from genericpath import isdir, isfile
from importlib import import_module
from os import listdir
from typing import Optional
# Rich
from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
# Core
from core.configreader import DataBaseConfig
from core.managers.logging import Log
from core.plugins.reader import PluginReader
from core.managers.user import UserManagement
# Extentions
from extentions.cli.helpers import find_filter


class CLIResponses():

    def __init__(self) -> None:
        """
        CLI Responses. Will respond to callen command
        """
        self.config = DataBaseConfig()

    def main_response(self):
        # Art logo
        art_str = "[red] _       ____________     ________  ________\n"\
            "[red]| |     / / ____/ __ )   / ____/  |/  / ___/\n" \
            "[red]| | /| / / __/ / __  |  / /   / /|_/ /\__ \ \n" \
            "[red]| |/ |/ / /___/ /_/ /  / /___/ /  / /___/ / \n" \
            "[red]|__/|__/_____/_____/   \____/_/  /_//____/  \n"

        print(Panel("[green] Web CMS Launching system... [/green] \n" + art_str,
                    title="[bold cyan] Web CMS [/bold cyan]", subtitle="[bold cyan] V 1.0.0 [/bold cyan]"))

    def get_configs_response(self, limit: int):
        # Define configs
        configurations = self.config.get_configs(limit)

        # define table
        table = Table(title="List of database configurations",
                      caption=f"Displaying {limit} rows")
        table.add_column("ID", style="cyan")
        table.add_column("name", style="yellow")
        table.add_column("value")

        for config in configurations:
            table.add_row(str(config.id), f"{config.name}", config.value)

        print(table)

    def create_config_response(self, name: str, value: str):
        """
        Creates config

        - name: str - Name of new config
        - value: str - Value of new config
        """
        configuration = self.config

        try:
            configuration.create_config(name, value)
            Log(f"Configuration [bold]{name}[/bold] created successfully with value [italic]{value}[/italic]", 3)

        except Exception:
            Log(f"Configuration named {name} already exists!", 2)

    def write_config_response(self, name: str, value: str):
        """
        Write existing config (Change value)
        ---

        - name: str - Name of existing config
        - value: str - New value of config
        """
        configuration = self.config

        try:
            configuration.write_config(name, value)
            Log(f"Value of configuration '{name}' successfuly changed to {value}", 3)

        except Exception:
            Log(f"Configuration named {name} not exists!", 2)

    def delete_config_response(self, name: str):
        """
        Delete an existing config
        ---

        - name: str - Name of existing config
        """
        configuration = self.config

        try:
            configuration.erase_config(name)
            Log(f"Successfully deleted configuration [bold]{name}[/bold]", 3)

        except Exception:
            Log(f"Configuration named {name} not exists!", 2)

    class Plugins():
        def list():
            # Main declarations
            list_of_dir = listdir("content/plugins")
            config = DataBaseConfig()

            # Active plugins
            active_plugins = config.get_parsed_config("active_plugins")

            # Table
            table = Table(title="List of plugins")

            # Adding columns
            table.add_column("ID", justify="center")
            table.add_column("dirname", style="red")
            table.add_column("path", style="yellow")

            for index, list_dir in enumerate(list_of_dir):
                if isdir(f"content/plugins/{list_dir}") and isfile(f"content/plugins/{list_dir}/plugin.py"):
                    if find_filter("name", list_dir, active_plugins):
                        table.add_row(
                            str(index), f"[green]{list_dir}[/green]", f"content/plugins/{list_dir}")
                    else:
                        table.add_row(str(index), list_dir,
                                      f"content/plugins/{list_dir}")

            print(table)

        def debug(name):
            plugin_exists = isdir(f"content/plugins/{name}")

            if plugin_exists and isfile(f"content/plugins/{name}/plugin.py"):
                module = import_module(f"content.plugins.{name}.plugin")

                # Initialize plugin
                try:
                    plugin = module.Plugin()
                    plugin.on_ready()

                    return plugin

                except Exception:
                    console = Console()
                    console.print_exception(show_locals=False)

            return Log(f"Plugin {name} not found in \"content/plugins\"!", 2)

        def read_information(plugin: str):
            # Initialize plugin reader
            reader = PluginReader()

            # Read manifest.json of plugin
            read_plugin = reader.read_plugin(plugin)

            table = Table(title=f"Information about plugin {plugin}")

            # Adding columns
            table.add_column("Display Name", style="green")
            table.add_column("Description", style="yellow")
            table.add_column("Keywords", style="cyan")

            # Adding rows
            table.add_row(read_plugin.name, read_plugin.description,
                          ",".join(read_plugin.meta))

            print(table)
            return table

    class User:
        def create(username: str, email: str, password: str):
            # Initialize user management
            user_manager = UserManagement()

            create_user = user_manager.create_user(username, email, password)

            return create_user
