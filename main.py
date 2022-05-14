# from flask import Flask
from core.application import app
from core.configparse import config
#

from core.bootup import boot_up


#
if __name__ == "__main__":
    boot_up()
    app.run(debug=config.getboolean("DEVELOPMENT", "Debug"), port=5001)
