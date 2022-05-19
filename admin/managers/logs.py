import datetime

from core.database.models.main import Logs, UserModel


class LogsManager:
    @classmethod
    def log(cls, user: UserModel):
        Logs.create(user=user,
                    timestamp=datetime.datetime.now())

    @classmethod
    def delete_log(cls):
        """
        метод не нужен т.к. небезопасно такое делать, а это вроде всё
        """
