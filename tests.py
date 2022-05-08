import os
import sys
import time
import unittest
from subprocess import Popen, PIPE


def catch_output(py_file: str, args: list):
    process = Popen([sys.executable, f"./{py_file}", *args], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    output = output.decode('utf8')
    return output


class TestingCMS(unittest.TestCase):
    def test_basic(self):
        # ТЕСТ СОЗДАН ДЛЯ МАШИНЫ ГИТХАБА ГДЕ ./crashreports ПУСТ
        f = open('config.ini', 'w+')
        f.write(
            '''[DATABASE]
Driver = Sqlite
Path = subconf.sqlite3

[DEVELOPMENT]
Debug = on''')
        f.close()
        os.system(f'"{sys.executable}" report.py -')
        self.assertEqual(1, len(os.listdir('./crashreports')),
                         msg=f"There is {len(os.listdir('./crashreports'))} crashreports instead of 1")
        out = catch_output("manager.py", ['createconfig', 'active_template', 'test'])
        self.assertIn('success', out.replace('\x1b[0m', ''), msg="error: " + out.replace('\x1b[0m', ''))
        catch_output("manager.py", ['createconfig', 'active_plugins', '[]'])
        # TODO: проверка на то что всё запустилось



if __name__ == '__main__':
    unittest.main()
