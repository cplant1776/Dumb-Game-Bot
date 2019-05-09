# Standard Library Imports
# Third Party Imports
# Local Imports
from src.actors.actions import Actions
from src.config import SETTINGS


class OutsideActions(Actions):
    """Contains Farmer's actions outside of the mission"""

    def __init__(self):
        super().__init__()

    # ==========================================
    # (1) Turn in Mission
    # ==========================================

    def turn_in_mission(self):
        """Sequence for turning in mission after exiting complete mission"""
        # click and search for contact dialog popup
        self.click_complete_mission_dialog()
        self.close_mission_window()
        self.close_additional_popup()
        pass

    def click_complete_mission_dialog(self):
        """Searches for specific dialog on screen and clicks it"""
        pass

    def close_mission_window(self):
        """Searches for specific dialog on screen and clicks it"""
        pass

    def close_additional_popup(self):
        """Clicks generic close button to close popup window"""
        pass

    # ==========================================
    # (2) Interact with Panel
    # ==========================================

    def walk_to_panel(self):
        """Moves forward up to the panel bench"""
        pass

    def click_while_searching_for_panel(self):
        """Clicks uniformly across the screen searching for the panel dialog"""
        pass

    # ==========================================
    # (3) Start Mission
    # ==========================================

    def click_play_button(self):
        """Clicks the play button to start the mission"""
        pass

    def click_accept_architect_mode(self):
        """Clicks on Yes for architect prompt"""
        pass

    def click_on_reward_type(self):
        """Clicks on reward type based on config settings (standard or architect)"""
        pass

    def close_architect_dialog(self):
        """Clicks generic close button to close popup window"""
        pass

    # ==========================================
    # (3) Walk to Contact
    # ==========================================

    def turn_around(self):
        """Turns the character left 180 degrees"""
        pass

    def target_contact(self):
        """Targets the contact via its name"""
        pass

    # ==========================================
    # (4) Accept Mission
    # ==========================================

    def open_contact_dialog(self):
        """Clicks around until contact dialog appears"""
        pass

    def click_accept_mission(self):
        """Clicks on the specific mission dialog to accept mission"""
        pass

    def close_contact_dialog(self):
        """Clicks generic close button to close popup window"""
        pass

    # ==========================================
    # (5) Enter Mission
    # ==========================================

    def click_while_searching_for_entrance(self):
        """Clicks around the edge of the screen searching for loading screen"""
        pass

    def move_closer_to_entrance(self):
        """Attempts to move closer to the entrance if couldn't find"""
        pass

