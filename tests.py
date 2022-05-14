import os
import sys
import unittest
from random import randint
from subprocess import Popen, PIPE

with open('config.ini', 'w+') as f:
    f.write('''[DATABASE]
Driver = Sqlite
Path = subconf.sqlite3

[DEVELOPMENT]
Debug = on''')

from core.database.crud.groups import GroupsCrud
from core.database.crud.users import UsersCrud
from core.managers.auth.user import UserManagement

from core.database.models.main import Configuration
from core.configreader import DataBaseConfig
from faker import Faker

fake = Faker()


def catch_output(py_file: str, args: list):
    process = Popen([sys.executable, f"./{py_file}", *args], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    output = output.decode('utf8')
    return output


class TestingCMS(unittest.TestCase):
    def test_crashes(self):
        os.system(f'"{sys.executable}" report.py -')
        self.assertEqual(1, len(os.listdir('./crashreports')),
                         msg=f"There is {len(os.listdir('./crashreports'))} crashreports instead of 1")
        # out = catch_output(
        #     "manager.py", ['createconfig', 'active_template', 'test'])

        # Create configurations
        database_config = DataBaseConfig()

        plugin_config = database_config.create_and_parse_config(
            "active_plugins", [])

        self.assertIsInstance(
            plugin_config, Configuration, msg="Failed to create plugin configuration")
        template_config = database_config.create_config(
            "active_template", "test")

        self.assertIsInstance(
            template_config, Configuration, msg="Failed to create template configuration")
        # проверка на то что всё запустилось никак т.к. гитхаб обрывает запуск сервера

    def test_user_system(self):
        Faker.seed(randint(1, 100))
        group = GroupsCrud.create(name=fake.user_name())
        user_manager = UserManagement()
        user = user_manager.create_user(username=fake.user_name(),
                                        email=fake.email(),
                                        password=fake.password())
        print(f"user created: {repr(user)}\n"
              f"group for him: {repr(group)}")
        self.assertEqual(user, UsersCrud.user_get(user.id),
                         msg="Found user in db is not equal to new user")
        self.assertFalse(user_manager.users_group_exists(user.id),
                         msg="New user has group, but shouldn't")
        UsersCrud.add_user_to_group(user.id, group.id)
        self.assertTrue(user_manager.users_group_exists(user.id),
                        msg=f"New user({repr(UsersCrud.user_get(user.id))}) has no group,"
                            f" but should have {repr(group)}")


if __name__ == '__main__':
    unittest.main()
