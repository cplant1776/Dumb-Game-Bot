# Standard Library Imports
# Third Party Imports
# Local Imports
from src.actors.actions import Actor
from src.actors.farmer_inside_actions import InsideActions
from src.actors.farmer_outside_actions import OutsideActions
from src.config import SETTINGS


class Farmer(Actor):
    """Controls character that will be completing the missions"""

    def __init__(self):
        super().__init__()
        self.inside_actions = InsideActions()
        self.outside_actions = OutsideActions()
