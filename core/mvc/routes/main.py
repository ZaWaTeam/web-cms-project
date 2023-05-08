from flask import send_from_directory
from core.application import app
from core.configreader import DataBaseConfig
from core.managers.lang import LanguageManager
from core.managers.logging import Log
from core.mvc.controllers.main import MainController, PageController, PostController
from defines import BASE_DIR

controllers = {"main": MainController(), "page": PageController(), "post": PostController()}
database_config = DataBaseConfig()
lm = LanguageManager()

Log(lm.get('bootup_router_init_main'), 0)


@app.route("/proj_stat/<path:filename>")
def static_folder(filename):
    return send_from_directory(f"{BASE_DIR}/content/theme/{database_config.get_config('active_template')}/static/", filename)


# Main Page
app.add_url_rule(rule=f'/',
                 view_func=controllers["main"].as_view("main_view"))

app.add_url_rule("/p", view_func=controllers["page"].as_view("page_view"))
app.add_url_rule("/b/{post_slug}", view_func=controllers["post"].as_view("post_view"))
