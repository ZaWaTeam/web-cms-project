import os
import sys

print("This script will setup dev version and it will run all tests")
os.system(f"{sys.executable} -m pip install -r requirements.txt")
os.system(f"{sys.executable} -m unittest")
