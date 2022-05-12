from flask import Response, render_template
from jinja2 import TemplateNotFound

from core.managers.logging import Log


class ControllersManager():

    def render_action(template_name, **context):
        try:
            return render_template(template_name, **context)

        except TemplateNotFound as e:
            Log(f"Template '{template_name}' not found", 2)
            return Response(f"<h3 style='font-family: Arial, sans-serif;'>Template '{template_name}' not found</h3>"
                            "<span style='font-family: Arial, sans-serif'>There is exception error in template render. Please check debug console</span>", 500)
