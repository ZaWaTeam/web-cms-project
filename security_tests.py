import os
import sys
import unittest
from random import randint
from subprocess import Popen, PIPE

from admin.managers.logs import LogsManager

with open('config.ini', 'w+') as f:
    f.write('''[DATABASE]
Driver = Sqlite
Path = subconf.sqlite3

[DEVELOPMENT]
Debug = on
HashTime = 13''')
from core.managers.auth.permissions import PermissionsManagement
from core.database.crud.groups import GroupsCrud
from core.database.crud.users import UsersCrud
from core.managers.auth.user import UserManagement

from core.database.models.main import Configuration, Permissions
from core.configreader import DataBaseConfig
from faker import Faker

fake = Faker()


class TestingSecurity(unittest.TestCase):
    def test_logs(self):
        Faker.seed(randint(1, 100))
        logs = LogsManager()
        logs.clear_logs()
        user_manager = UserManagement()
        user = user_manager.create_user(username=fake.user_name(),
                                        email=fake.email(),
                                        password=fake.password())
        print(f"user created: {repr(user)}\n")
        data1 = fake.pydict()
        logs.log(user, str(data1))
        data2 = fake.pydict()
        logs.log(user, str(data2))
        print(logs.get_logs())
        log1, log2 = logs.get_logs()
        self.assertEqual(log1.raw_data, str(data1))
        self.assertEqual(log2.raw_data, str(data2))


if __name__ == '__main__':
    unittest.main()
