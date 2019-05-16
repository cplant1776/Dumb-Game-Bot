# Standard Library Imports
# Third Party Imports
# Local Imports
from src.actors.actions import Actor
from src.config import SETTINGS


class Leveler(Actor):
    """Controls character that will be leveling up"""

    def __init__(self):
        super().__init__()
