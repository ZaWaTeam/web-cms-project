from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from core.configreader import DataBaseConfig
from defines import BASE_DIR

config = DataBaseConfig()

main_template = config.get_config("active_template")

app = Flask(__name__, template_folder=f"{BASE_DIR}/content/theme/{main_template}",
            static_folder=f"{BASE_DIR}/content/theme")
CORS(app)
api = Api(app, "/api/admin")

# Registering admin RestAPI Endpoint
