import datetime

from core.database.connect import CpDb
from core.database.models.main import Logs, UserModel


# noinspection SqlWithoutWhere
class LogsManager:
    @classmethod
    def log(cls, user: UserModel, raw_data: str):
        return Logs.create(user=user,
                           raw_data=raw_data,
                           timestamp=datetime.datetime.now())

    @classmethod
    def delete_log(cls):
        """
        метод не нужен т.к. небезопасно такое делать, а это вроде всё
        """

    @classmethod
    def get_logs(cls):
        logs = [log for log in Logs.select()]
        return logs

    @classmethod
    def clear_logs(cls):
        cur = CpDb.execute_sql('DELETE FROM logs')
        return cur.fetchall()
