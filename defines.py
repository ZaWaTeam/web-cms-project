import os

# Define base dir. Constant to root dir
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ACTIONS = [
    "get_post",
    "get_posts",
    "get_category",
    "get_categories"
]

# Permissions


class PERMISSIONS:

    WEBCMS = "webcms"

    # Control panel
    LOGIN_TO_PANEL = f"{WEBCMS}.panel"
