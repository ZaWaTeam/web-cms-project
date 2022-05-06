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
        art_str = "[red]  ____       __               __        ________   _______  _______ \n"\
            "[red] /_  / ___ _/ /  _______  ___/ /__ ____|_  / / /  / ___/  |/  / __/ \n" \
            "[red]  / /_/ _ `/ _ \/ __/ _ \/ _  / -_) __//_ <_  _/ / /__/ /|_/ /\ \   \n" \
            "[red] /___/\_,_/_//_/\__/\___/\_,_/\__/_/ /____//_/   \___/_/  /_/___/   \n"

        print(Panel("[green] Zahcoder34 CMS Launching system... [/green] \n" + art_str,
                    title="[bold cyan] Zahcoder34 CMS [/bold cyan]", subtitle="[bold cyan] V 1.0.0 [/bold cyan]"))

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
