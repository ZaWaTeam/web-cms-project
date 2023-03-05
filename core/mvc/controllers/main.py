from flask import render_template, request, abort, send_from_directory
from flask.views import View

from core.managers.controllers import ControllersManager
from defines import BASE_DIR

class FaviconController(View):

    def dispatch_request(self):

        # Template
        return send_from_directory(f"{BASE_DIR}", 'favicon.ico')
class MainController(View):

    def dispatch_request(self):

        # Template
        return ControllersManager.render_action(f"index.html")




class PageController(View):

    def dispatch_request(self):
        """
        The dispatch_request function is a method of the Flask class. It is responsible for handling all requests made to
        the application, and dispatching them to the right view function. The dispatch_request function takes in an argument
        called self, which is a reference to the current instance of our app object (app). This allows us to access attributes
        of our app object such as config settings and other methods we have defined on it.

        :param self: Access variables that belongs to the class
        :return: HTTP RESPONSE
        """
        page = request.args.get("p")
        # Render template
        if not page:
            return abort(404)

        return ControllersManager.render_action(template_name=f"content/page.html", page=page)


class PostController(View):

    def dispatch_request(self, category, post):
        return render_template(f"contents/post.html")


class ListController(View):

    def dispatch_request(self, page):
        return render_template(f"contents/lists.html")
