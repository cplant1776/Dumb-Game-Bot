# Standard Library Imports
# Third Party Imports
# Local Imports
from src.actors.farmer import Farmer
from src.actors.leveler import Leveler
from src.config import SETTINGS


class Coordinator:
    """Coordinates actions of both Farmer and Leveler"""

    def __init__(self):
        self.farmer = Farmer()
        self.leveler = Leveler()

    def run(self):
        """Repeatedly clears the mission until configured number of runs is reached"""
        # Initiate as Farmer inside

        # LOOP
        # Have farmer clear mission
        # Switch actors
        # Leveler exit mission
        # Switch actors
        # Farmer prepares next mission
        # Switch actors
        # Leveler enters mission
        # Switch actors
        # Confirm Farmer has loaded
        # LOOP
        pass

    def switch_actors(self):
        """Switches between active actor. If Farmer active, switches to Leveler and vice versa"""
        pass

    # ===========================================
    # Farmer
    # ===========================================
    def farmer_clear_mission(self):
        """Returns after Farmer has cleared and exited mission"""
        # Run interior cycle
        # Click exit button
        pass

    def farmer_prepares_next_mission(self):
        """Returns after farmer has successfully started next mission and entered loading screen"""
        # Turn in mission
        # Move to bench
        # Start mission
        # Move to contact
        # Talk to contact
        # Enter mission
        pass

    def check_if_loading_done(self):
        """Returns after Farmer detects non-loading screen element"""
        pass

    # ===========================================
    # Leveler
    # ===========================================
    def leveler_exit_mission(self):
        """Returns after Leveler finishes loading"""
        # Make Leveler click exit button
        # Wait for non-loading screen
        pass

    def leveler_enters_mission(self):
        """Returns after leveler has finished loading into mission"""
        # Leveler turn around
        # Leveler enter mission
        # Wait for non-load screen
        pass


