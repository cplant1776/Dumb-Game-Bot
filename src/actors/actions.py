# Standard Library Imports
from threading import Thread
from time import sleep
# Third Party Imports
import keyboard
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon
from src.imagesearch import *
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

    @staticmethod
    def click(pos=(0, 0)):
        """Sends a click command to the target coordinates, pos"""
        pyautogui.click(x=pos[0], y=pos[1])

    def click_periodically(self, pos=(0, 0), interval=1, duration=1):
        """Sends a click command to the given coordinates every given interval for given duration"""
        time_passed = 0
        while time_passed < duration/interval:
            self.click(pos=pos)
            sleep(interval)
            time_passed += interval

    def click_img(self, target_img):
        """Searches for a target image and clicks at its location"""
        pos = imagesearch_loop(target_img, timesample=0.5)
        if pos[0] == -1:
            print("No image found")
        else:
            self.click(pos)

    def click_randomly_in_area(self, num_of_clicks, region, interval=0.5, img=None):
        """
        Clicks randomly within a passed polygon on the screen, pausing X sec between clicks

        args
        num_of_clicks - how many times to click the area
        region - shapely Polygon that contains the search area
        interval - how often to click
        img - Optional image to search for. If passed, the function will return when it finds the image

        """
        # Generate coordinates to click at
        click_points = self.generate_random_points_in_polygon(num_of_clicks, region)
        click_points = self.convert_shapely_points_to_tuples(click_points)
        for point in click_points:
            # Click point
            self.click(point)
            # Check for image
            if img:
                pos = imagesearch(img)
                # Return if image found
                if pos[0] != -1:
                    return
            # Wait
            sleep(interval)

    @staticmethod
    def generate_random_points_in_polygon(num_of_points, polygon) -> list:
        """Returns a list of (num_of_points) (x,y) tuples contained within the given polygon"""
        list_of_points = []
        min_x, min_y, max_x, max_y = polygon.bounds
        counter = 0
        while counter < num_of_points:
            point = Point(random.uniform(min_x, max_x), random.uniform(min_y, max_y))
            if polygon.contains(point):
                list_of_points.append(point)
                counter += 1
        return list_of_points

    @staticmethod
    def convert_shapely_points_to_tuples(list_of_points) -> list:
        """Converts a list of Points to a list of (x, y) tuples"""
        return [(p.x, p.y) for p in list_of_points]

    def click_while_searching_for_img(self, target_img, target_area):
        """Clicks an area until it sees the target img pop up"""
        pass

    def click_close_button(self):
        """Clicks the generic close button present on many menus"""
        self.click_img(target_img=SETTINGS['img_paths']['buttons']['close'])

    def click_exit_button(self):
        """Clicks button to exit mission"""
        self.click_img(target_img=SETTINGS['img_paths']['buttons']['exit'])

    def run_periodic_clicking_thread(self, pos, interval, duration):
        t = Thread(target=self.click_periodically, args=[pos, interval, duration])
        t.run()

    # =================================
    # Movement
    # =================================

    def move(self, direction='forward', duration=0.0):
        """Moves the character in given direction for the given duration


        arguments
        ---------
        direction - accepts "left", "right", "forward", "backward" and uses it as dict key for self.move_dir
        duration - how long to hold the movement key
        """
        # Depress proper movement key
        keyboard.press(self.move_dir[direction])

        # After duration, release key
        if duration > 0.0:
            sleep(duration)
            keyboard.release(self.move_dir[direction])

    def turn(self, direction='left', degrees=0):
        """
        Turns a given number of degrees in the given direction

        arguments
        ---------
        direction - accepts "left" or "right" and uses it as dict key for self.turn_dir
        degrees - number of degrees you wish to turn the character

        """
        duration_of_turn = self.degrees_to_duration(degrees)
        # Depress proper turn key
        keyboard.press(self.turn_dir[direction])

        # After duration, release key
        if duration_of_turn > 0.0:
            sleep(duration_of_turn)
            keyboard.release(self.move_dir[direction])

    @staticmethod
    def move_to_target():
        """Auto-follows the current target, causing the character to constantly move toward them"""
        keyboard.send('f')
        pass

    def turn_while_clicking(self, direction, interval, degrees, pos):
        """Turns given number of degrees in given direction while clicking at given position"""
        duration_of_turn = self.degrees_to_duration(degrees)
        self.run_periodic_clicking_thread(pos=pos, interval=interval, duration=duration_of_turn)
        self.turn(direction=direction, degrees=degrees)

    @staticmethod
    def degrees_to_duration(degrees):
        """Converts a given degrees into a duration given that it takes X sec to turn 360 degrees"""
        return degrees / (360 / SETTINGS['time_for_full_turn'])

    # =================================
    # Targeting
    # =================================

    @staticmethod
    def target_by_name(name=''):
        """Attempts to target entity with given name in character's field of vision"""
        keyboard.send('enter, /target_custom_near {}, enter', name)

    @staticmethod
    def target_nearest_enemy():
        """Targets the enemy closest to the character and in the camera's field of vision"""
        keyboard.send('ctrl+tab')

    # =================================
    # Waiting
    # =================================

    @staticmethod
    def wait_for_non_loading_screen():
        """Periodically searches for non-loading screen elements and returns True when found"""
        imagesearch_loop(image=SETTINGS['img_paths']['screens']['nav_box'])
