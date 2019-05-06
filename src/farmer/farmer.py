# Standard Library Imports
# Third Party Imports
# Local Imports
from src.farmer.farmer_inside_actions import InsideActions
from src.farmer.farmer_outside_actions import OutsideActions


class Farmer:
    """Controls character that will be completing the missions"""

    def __init__(self):
        self.inside_actions = InsideActions()
        self.outside_actions = OutsideActions()
