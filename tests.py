import os
import sys
import unittest
from subprocess import Popen, PIPE
with open('config.ini', 'w+') as f:
    f.write('''[DATABASE]
Driver = Sqlite
Path = subconf.sqlite3

[DEVELOPMENT]
Debug = on''')
from core.database.models.main import Configuration
from core.configreader import DataBaseConfig


def catch_output(py_file: str, args: list):
    process = Popen([sys.executable, f"./{py_file}", *args], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    output = output.decode('utf8')
    return output


class TestingCMS(unittest.TestCase):
    def test_basic(self):
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
        # catch_output("manager.py", ['createconfig', 'active_plugins', '[]'])
        # TODO: проверка на то что всё запустилось


if __name__ == '__main__':
    unittest.main()