from flask import Blueprint, Flask

from core.configreader import DataBaseConfig
from defines import BASE_DIR

config = DataBaseConfig()

main_template = config.get_config("active_template")

app = Flask(__name__, template_folder=f"{BASE_DIR}/content/theme/{main_template}",
            static_folder=f"{BASE_DIR}/content/theme")

# Admin blueprint
admin = Blueprint("ControlPanel",
                  __name__, template_folder=f"{BASE_DIR}/core/admin/template", static_folder=f"{BASE_DIR}")

# Registering admin blueprint
app.register_blueprint(admin)
