from flask import Blueprint, Flask

from core.configreader import DataBaseConfig
from defines import BASE_DIR

config = DataBaseConfig()

main_template = config.get_config("active_template")

app = Flask(__name__, template_folder=f"{BASE_DIR}/content/theme/{main_template}",
            static_folder=f"{BASE_DIR}/content/theme")

# Admin blueprint
admin = Blueprint("cpanel",
                  __name__, template_folder=f"{BASE_DIR}/admin/template", static_folder=f"{BASE_DIR}/admin/template/assets", url_prefix="/cpanel")

# Registering admin blueprint
