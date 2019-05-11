# Standard Library Imports
from threading import Thread
from time import sleep
# Third Party Imports
# Local Imports
from src.config import SETTINGS


class Actor:
    """Parent class with common attributes between Leveler and Farmer"""
    def __init__(self):
        self.actions = Actions()


class Actions:
    """Contains basic actions shared by actors (Farmer, Leveler)"""

    def __init__(self):
        self.move_dir = {'forward': 'W',
                         'backward': 'S',
                         'left': 'A',
                         'right': 'D'}

        self.turn_dir = {'left': 'Q',
                         'right': 'E'}

    # =================================
    # Clicks
    # =================================

    def click(self, pos=(0, 0)):
        """Sends a click command to the target coordinates, pos"""
        pass

    def click_periodically(self, pos=(0, 0),interval=1, duration=1):
        """Sends a click command to the given coordinates every given interval for given duration"""
        time_passed = 0
        while time_passed < duration/interval:
            self.click(pos=pos)
            sleep(interval)
            time_passed += interval

    def click_while_searching_for_img(self, target_img, target_area):
        """Clicks an area until it sees the target img pop up"""
        pass

    def search_for_img_and_click(self, target_img):
        """Searches for a target image and clicks at its location"""
        pass

    def click_close_button(self):
        """Clicks the generic close button present on many menus"""
        pass

    def click_exit_button(self):
        """Clicks button to exit mission"""
        pass

    # =================================
    # Movement
    # =================================

    def move(self, direction='forward', duration=1):
        """Moves the character in given direction for the given duration"""
        pass

    def turn(self, direction='left', degrees=0):
        """
        Turns a given number of degrees in the given direction
        It takes ~5 sec to turn 360 degrees. We convert the degrees to turn duration based on this assumption.

        arguments
        ---------
        direction - accepts "left" or "right" and uses it as dict key for self.turn_dir
        degrees - number of degrees you wish to turn the character

        """
        pass

    def move_to_target(self):
        """Auto-follows the current target, cuasing the character to constantly move toward them"""
        pass

    def turn_while_clicking(self, direction, interval, degrees, pos):
        """Turns given number of degrees in given direction while clicking at given position"""
        duration_of_turn = degrees/72  # 72 degrees ~= 1 sec
        t = Thread(target=self.click_periodically, args=[pos, interval, duration_of_turn])
        t.run()
        self.turn(direction=direction, degrees=degrees)

    # =================================
    # Targeting
    # =================================

    def target_by_name(self, name=''):
        """Attempts to target entity with given name in character's field of vision"""
        pass

    def target_nearest_enemy(self):
        """Targets the enemy closest to the character and in the camera's field of vision"""
        pass

    # =================================
    # Waiting
    # =================================

    def wait_for_non_loading_screen(self):
        """Periodically searches for non-loading screen elements and returns True when found"""
        pass
