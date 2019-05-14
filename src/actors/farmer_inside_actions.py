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
        pass

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
        # Turn left 360 degrees while searching for target in a separate thread
        t = Thread(target=self.turn, args=['left', 360])
        t.run()
        # If target found, return
        start = time.time()
        while time.time() < start + SETTINGS['time_for_full_turn']:
            # TODO: Refactor inner loop to a function that returns if pos != 1
            for enemy_type in SETTINGS['img_paths']['health']['full'].values():
                pos = imagesearch(enemy_type)
        # else, loop while no target found (1) turn left 120 degrees (2) move forward ~2 sec (3) search for target

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



