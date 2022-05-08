from datetime import datetime

from rich.console import Console
from rich.traceback import install

from core.managers.exceptions import LogTypeValueError


class LoggingManager:

    console = Console(log_time_format="%a, %d %b %Y %H:%M:%S")

    def __init__(self) -> None:
        console = Console(log_time_format="%a, %d %b %Y %H:%M:%S")
        install(console=console, show_locals=True, width=110)

    def use_log(self, path, mode):
        pass

    def create_info_log(self, log: str):
        self.console.print(
            f"[[dim cyan]info {str(datetime.now())}[/dim cyan]] [cyan]{log}[/cyan]")

        return True

    def create_warning_log(self, log: str):
        self.console.print(
            f"[[dim yellow]warning {str(datetime.now())}[/dim yellow]] [yellow]{log}[/yellow]")

        return True

    def create_error_log(self, log: str):
        self.console.print(
            f"[[dim red]error {str(datetime.now())}[/dim red]] [red]{log}[/red]")

        return True

    def create_success_log(self, log: str):
        self.console.print(
            f"[[dim green]success {str(datetime.now())}[/dim green]] [green]{log}[/green]")

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
        super().__init__()
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
