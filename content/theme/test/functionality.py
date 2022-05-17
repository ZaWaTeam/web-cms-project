from core.managers.theme import ThemeManager


class ThemeFunctionality(ThemeManager):
    # Theme definition
    theme_name: str = "test"
    theme_description: str = "some description"
    theme_keywords: list = ["test", "something", "otherthing"]

    # functions

    def on_load(self):
        """
        The on_load function is called when the page is loaded. It loads all of the static files (CSS, JS) and creates editable elements.

        :param self: Access fields in the class
        :return: None
        """
        static = {
            "css": ["css/main.css"],
            "js": ["js/main.js"]
        }
        editables: list[dict] = [{"name": "MainText",
                                  "default": "Hello world", "type": 0},
                                 {
                                     "name": "MainArray",
                                     "default": ["Hello world1", "Hello world2"],
                                     "type": 1
                                 }]

        self.load_static(static)

        # Create editables
        self.create_editable(editables)

    def create_editable(self, editables):
        for editable in editables:
            self.define_editable(
                editable["name"], editable["default"], editable["type"])
