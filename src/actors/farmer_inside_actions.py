# Standard Library Imports
# Third Party Imports
# Local Imports
from src.actors.actions import Actions
from src.config import SETTINGS


class InsideActions(Actions):
    """Contains Farmer's actions inside of the mission"""

    def __init__(self):
        super().__init__()

    # ===========================================
    # (1) Load into mission
    # ===========================================

    def search_for_non_loading_screen(self):
        """Periodically checks if the map has finished loading"""
        pass

    def target_initial_enemy(self):
        """Attempts to target the best initial target by turning character left ~120 degrees"""
        pass

    # ===========================================
    # (2) Start Interior Cycle
    # ===========================================

    def run_interior_cycle(self):
        """Continuously cycles between attack and searching for enemies until mission exit button is found"""
        # Move to target
        # Launch attack cycle till no targets found
        # Search for mission completion button
        # Launch search cycle
        pass

    # ===========================================
    # (2.a) Attack
    # ===========================================

    def attack_cycle(self):
        """Repeatedly cycles through attacks while moving to target until no targets are left"""
        # Target nearest
        # Return if no target found
        # Else move to target
        # Cycle through attacks
        pass

    def cycle_through_abilities(self):
        """Cycles through the powers on Farmer's 1st action bar from 1-n, where n is set in config file"""
        pass

    # ===========================================
    # (2.b) Search for Enemies if None Found
    # ===========================================

    def search_cycle(self):
        """Attempts to find any remaining enemies on the map by moving around it"""
        # Turn left 360 degrees while searching for target
        # If target found, return
        # else, loop while no target found (1) turn left 120 degrees (2) move forward ~2 sec (3) search for target
        pass

    # ===========================================
    # (2.c) Search for Mission Completion
    # ===========================================
    def search_for_mission_completion(self):
        """Searches for presence of mission exit button and clicks it if found"""
        pass



