# Standard Library Imports
# Third Party Imports
from src.imagesearch import *
import keyboard
from threading import Thread
import time

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

    @staticmethod
    def search_for_non_loading_screen():
        """Periodically checks if the map has finished loading"""
        imagesearch_loop(image=SETTINGS['img_paths']['screens']['nav_box'])

    def target_initial_enemy(self):
        """Attempts to target the best initial target by turning character left ~120 degrees"""
        self.turn(direction='left', degrees=120)

    # ===========================================
    # (2) Start Interior Cycle
    # ===========================================

    def run_interior_cycle(self):
        """Continuously cycles between attack and searching for enemies until mission exit button is found"""
        is_complete = False
        while not is_complete:
            # Move to target
            self.move_to_target()
            # Launch attack cycle till no targets found
            self.attack_cycle()
            # Search for mission completion button
            is_complete = self.search_for_mission_completion()
            # Launch search cycle
            self.search_cycle()

    # ===========================================
    # (2.a) Attack
    # ===========================================

    def attack_cycle(self):
        """Repeatedly cycles through attacks while moving to target until no targets are left"""
        target_found = self.target_was_found()
        while target_found:
            # Target nearest
            self.target_nearest_enemy()
            # End loop if no target found
            target_found = self.target_was_found()
            # Attempt move to target
            self.move_to_target()
            # Cycle through attacks
            self.cycle_through_abilities()

    @staticmethod
    def cycle_through_abilities():
        """Cycles through the powers on Farmer's 1st action bar from 1-n, where n is set in config file"""
        for i in range(1, SETTINGS['max_attack_key'] + 1):
            keyboard.send(str(i))
            time.sleep(0.5)

    @staticmethod
    def target_was_found():
        pos = imagesearch(SETTINGS['img_paths']['no_target'])
        # TODO: Check for potential bug. Reverse T/F?
        if pos[0] != -1:
            print("No target found")
            return True
        return False

    # ===========================================
    # (2.b) Search for Enemies if None Found
    # ===========================================

    def search_cycle(self):
        """Attempts to find any remaining enemies on the map by moving around it"""
        # Turn left 360 degrees while searching for target
        target_found = self.turn_and_search(direction='left', degrees=360,
                                            target_images=SETTINGS['img_paths']['health_full'])
        # Keep moving around map until a new target is located
        while not target_found:
            # turn left 120 degrees while searching for target
            target_found = self.turn_and_search(direction='left', degrees=120,
                                                target_images=SETTINGS['img_paths']['health_full'])
            self.move(direction='forward', duration=2)

    def turn_and_search(self, direction, degrees, target_images) -> bool:
        """Turn given direction for given number of degrees while searching for given target images"""
        duration_of_turn = self.degrees_to_duration(degrees)
        # Depress proper turn key
        keyboard.press(self.turn_dir[direction])

        start = time.time()
        img_found = False
        # Search for target images while turning
        while (time.time() < start + duration_of_turn) or img_found is False:
            # Search for enemy
            self.target_nearest_enemy()
            for img in target_images:
                pos = imagesearch(img)
                if pos[0] != -1:
                    img_found = True
            # Wait before next search
            time.sleep(SETTINGS['time_between_image_searches'])
        # Release key after timeout or if img found before then
        keyboard.release(self.move_dir[direction])
        return img_found

    # ===========================================
    # (2.c) Search for Mission Completion
    # ===========================================
    @staticmethod
    def search_for_mission_completion():
        """Searches for presence of mission exit button and clicks it if found"""
        pos = imagesearch(SETTINGS['img_paths']['buttons']['exit'])
        if pos[0] == -1:
            return False
        else:
            return True



