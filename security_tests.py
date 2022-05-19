import unittest

from flask import Request
import mock
with open('config.ini', 'w+') as f:
    f.write('''[DATABASE]
Driver = Sqlite
Path = subconf.sqlite3

[DEVELOPMENT]
Debug = on
HashTime = 13''')
from admin.managers.security import SecurityManager
from faker import Faker

fake = Faker()


class TestingSecurity(unittest.TestCase):
    def test_admin_security(self):
        mk = mock.MagicMock()
        mk.cookies = 'auth=test'
        with mock.patch("admin.managers.security.SecurityManager.request", mk):
            self.assertFalse(SecurityManager.user_authenticated())



if __name__ == '__main__':
    unittest.main()
