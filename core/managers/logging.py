from datetime import datetime
from rich.traceback import install
from rich import print as console_output
from core.managers.exceptions import LogTypeValueError


class LoggingManager():
    def __init__(self) -> None:
        install()

    def use_log(self, path, mode):
        pass

    def create_info_log(self, log: str):
        output = console_output(
            f"[[dim cyan]info {str(datetime.now())}[/dim cyan]] [cyan]{log}[/cyan]")

        return True

    def create_warning_log(self, log: str):
        output = console_output(
            f"[[dim yellow]warning {str(datetime.now())}[/dim yellow]] [yellow]{log}[/yellow]")

        return True

    def create_error_log(self, log: str):
        output = console_output(
            f"[[dim red]error {str(datetime.now())}[/dim red]] [red]{log}[/red]")

        return True

    def create_success_log(self, log: str):
        output = console_output(
            f"[[dim green]error {str(datetime.now())}[/dim green]] [green]{log}[/green]")

        return True


class Log(LoggingManager):
    def __init__(self, output: str, type: int) -> None:
        """
        Display and save log.
        -------------------

        Available types:
            - `0`: Info log. Prefix `[info]: log`
            - `1`: Warning log. Prefix `[warning]: log`. Colors `Yellow`
            - `2`: Error log. Prefix `[error]: log`. Colors `Red`
            - `3`: Success log. Prefix `[success]: log`. Colors `Lime`
        """
        if type == 0:
            self.create_info_log(output)

        elif type == 1:
            self.create_warning_log(output)

        elif type == 2:
            self.create_error_log(output)

        elif type == 3:
            self.create_success_log(output)

        else:
            raise LogTypeValueError(
                f"There is no registered log type index {type}")
