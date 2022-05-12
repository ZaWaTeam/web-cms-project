from flask import send_from_directory
from core.application import app
from core.configreader import DataBaseConfig
from core.managers.logging import Log
from core.mvc.controllers.main import MainController, PageController
from defines import BASE_DIR

controllers = {"main": MainController(), "page": PageController()}
database_config = DataBaseConfig()

Log("Successfully initialized router [bold]main[/bold]", 0)


@app.route("/proj_stat/<path:filename>")
def static_folder(filename):
    return send_from_directory(f"{BASE_DIR}/content/theme/{database_config.get_config('active_template')}/static/", filename)


# Main Page
app.add_url_rule(rule=f'/',
                 view_func=controllers["main"].as_view("main_view"))

app.add_url_rule("/page", view_func=controllers["page"].as_view("page_view"))
