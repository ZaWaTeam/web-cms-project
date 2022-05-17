from core.application import admin
from .controllers import dashboard, auth, plugins, settings, themes

controllers = {}

admin.add_url_rule("/")
