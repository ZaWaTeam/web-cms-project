from time import sleep
import rich
from typing import Optional, List
import typer

from core.managers.logging import Log
from .responses import CLIResponses

app = typer.Typer()
responses = CLIResponses()


@app.command()
def main():
    responses.main_response()


@app.command()
def configs(limit: int = typer.Argument(20)):
    responses.get_configs_response(limit)


@app.command()
def createconfig(name: str, value: str):
    responses.create_config_response(name, value)


@app.command()
def writeconfig(name: str, value: str):
    responses.write_config_response(name, value)


@app.command()
def deleteconfig(name: str):
    responses.delete_config_response(name=name)


"""
Plugins
"""


@app.command()
def pluginlist():
    responses.Plugins.list()


@app.command()
def plugindebug(name: str):
    plugin = responses.Plugins.debug(name=name)

    while True:
        try:
            pass

        except KeyboardInterrupt:
            Log("Stopping plugin work...", 0)
            plugin.on_disable()
            sleep(0.5)

            raise typer.Abort()


@app.command()
def readplugin(plugin: str):
    plugin = responses.Plugins.read_information(plugin)


"""
User Management
"""


@app.command()
def createuser(username: str, email: str, password: str):
    try:
        create_user = responses.User.create(username, email, password)

        if create_user:
            Log(f"User {username} created successfully!", 3)

    except Exception as e:
        Log(f"Failed to create user {username}, due to {e}", 2)
