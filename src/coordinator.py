# Standard Library Imports
# Third Party Imports
# Local Imports
from src.farmer.farmer import Farmer
from src.leveler import Leveler


class Coordinator:
    """Coordinates actions of both Farmer and Leveler"""

    def __init__(self, img_paths):
        self.paths = img_paths
        self.farmer = Farmer()
        self.leveler = Leveler()
