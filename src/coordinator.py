# Standard Library Imports
# Third Party Imports
import keyboard
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
        n = 1
        while n <= SETTINGS['number_of_runs']:
            print("Starting run {}".format(n))
            # Have farmer clear mission
            self.do_event_then_switch_actors(self.farmer_prepares_next_mission)
            # Leveler exit mission
            self.do_event_then_switch_actors(self.leveler_exit_mission)
            # Farmer prepares next mission
            self.do_event_then_switch_actors(self.farmer_prepares_next_mission)
            # Leveler enters mission
            self.do_event_then_switch_actors(self.leveler_enters_mission)
            # Confirm Farmer has loaded
            self.do_event_then_switch_actors(self.farmer_check_if_loading_done)
            n += 1
        return

    @staticmethod
    def switch_actors():
        """Switches between active actor. If Farmer active, switches to Leveler and vice versa"""
        keyboard.send('alt+tab')

    def do_event_then_switch_actors(self, run_event):
        """Executes the passed function and then switches active actor"""
        result = run_event()
        self.switch_actors()
        return result

    # ===========================================
    # Farmer
    # ===========================================
    def farmer_clear_mission(self):
        """Returns after Farmer has cleared and exited mission"""
        # Run interior cycle
        self.farmer.inside_actions.run_interior_cycle()
        # Click exit button
        self.farmer.actions.click_exit_button()

    def farmer_prepares_next_mission(self):
        """Returns after farmer has successfully started next mission and entered loading screen"""
        # Turn in mission
        self.farmer.outside_actions.turn_in_mission()
        # Move to Panel and open menu
        self.farmer.outside_actions.interact_with_panel()
        # Start mission
        self.farmer.outside_actions.start_mission()
        # Move to contact
        self.farmer.outside_actions.move_to_contact()
        # Talk to contact
        self.farmer.outside_actions.accept_mission()
        # Enter mission
        self.farmer.outside_actions.enter_mission()

    def farmer_check_if_loading_done(self):
        """Returns after Farmer detects non-loading screen element"""
        self.farmer.actions.wait_for_non_loading_screen()

    # ===========================================
    # Leveler
    # ===========================================
    def leveler_exit_mission(self):
        """Returns after Leveler finishes loading"""
        # Make Leveler click exit button
        self.leveler.actions.click_exit_button()
        # Wait for non-loading screen
        self.leveler.actions.wait_for_non_loading_screen()

    def leveler_enters_mission(self):
        """Returns after leveler has finished loading into mission"""
        # Leveler turn around and enter mission
        self.leveler.actions.turn_while_clicking(direction='left', interval=0.3, degrees=180, pos=SETTINGS['center']['top'])
        # Wait for non-load screen
        self.leveler.actions.wait_for_non_loading_screen()


