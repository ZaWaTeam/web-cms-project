from flask import render_template, request, abort
from flask.views import View
from core.configreader import DataBaseConfig
from core.managers.controllers import ControllersManager


class MainController(View):

    def dispatch_request(self):

        # Template
        return ControllersManager.render_action(f"index.html")


class PageController(View):

    def dispatch_request(self):
        page = request.args.get("p")
        # Render template
        if not page:
            return abort(404)

        return ControllersManager.render_action(f"content/page.html", page=page)


class PostController(View):

    def dispatch_request(self, category, post):
        return render_template(f"contents/post.html")


class ListController(View):

    def dispatch_request(self, page):
        return render_template(f"contents/lists.html")
