import getpass
import os
import sys
from datetime import datetime
from subprocess import Popen, PIPE

process = Popen([sys.executable, "./main.py"], stdout=PIPE)
(output, err) = process.communicate()
exit_code = process.wait()
output = output.replace(b'\x85', b'').decode('utf8')
if len(sys.argv) == 1:
    print(output)  # выводим в том случае если к програме не было никаких аргументов
if "Traceback (most recent call last)" in output:
    with open(f"crashreports/crash-{str(datetime.now()).replace(' ', 'b').replace(':', '.')[:-7]}.txt", 'w+',
              encoding='utf8') as f:
        f.write(output.replace('\n', '').replace("[0m", '').replace(getpass.getuser(), ''))
        cf = open('config.ini', 'r', encoding='utf8')
        f.write("\nCONFIG:\n\n")
        f.write(cf.read())
