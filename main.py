# from flask import Flask
from core.application import app
#

import core.bootup


#
if __name__ == "__main__":
    app.run(debug=True)
