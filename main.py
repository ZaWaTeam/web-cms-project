# from flask import Flask
from core.application import app
from core.configparse import config
#

import core.bootup


#
if __name__ == "__main__":
    app.run(debug=config.getboolean("DEVELOPMENT", "Debug"))
