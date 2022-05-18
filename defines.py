import os

# Define base dir. Constant to root dir
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Permissions


class PERMISSIONS:

    WEBCMS = "webcms"

    # Control panel
    LOGIN_TO_PANEL = f"{WEBCMS}.panel"
