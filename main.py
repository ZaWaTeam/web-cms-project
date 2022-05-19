# from flask import Flask
from core.application import app, admin
from core.configparse import config
#

from core.bootup import boot_up


#
if __name__ == "__main__":
    boot_up()

    # Admin blueprint
    app.register_blueprint(admin)

    # App launch
    app.run(debug=config.getboolean("DEVELOPMENT", "Debug"), host=config.get(
        "DEVELOPMENT", "Host"), port=config.get("DEVELOPMENT", "Port"))
