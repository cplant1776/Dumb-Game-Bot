# Standard Library Imports
# Third Party Imports
# Local Imports
from src.config import SETTINGS
from src.coordinator import Coordinator


# ==============================================================
# Main
# ==============================================================
if __name__ == '__main__':
    app = Coordinator()
    app.run()
    print("hi!")
