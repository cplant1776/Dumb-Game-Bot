# Standard Library Imports
from ctypes import windll
# Third Party Imports
from os.path import abspath, join
from shapely.geometry import Polygon
from yaml import FullLoader, load
# Local Imports


# ==============================================================
# Import Settings From config.yaml
# ==============================================================
def convert_config_paths(config):
    """Convert paths from the yaml config to local OS format"""
    for branch in config['img_paths'].values():
        if type(branch) == dict:
            for k, v in branch.items():
                branch[k] = abspath(v)


def import_config_settings() -> dict:
    """Import yaml file as dictionary"""
    try:
        with open('config.yaml', 'r') as f:
            result = load(f, Loader=FullLoader)
            convert_config_paths(result)
    except FileNotFoundError:
        with open(join('..', '..', 'config.yaml'), 'r') as f:
            result = load(f, Loader=FullLoader)
            convert_config_paths(result)
    return result


def generate_screen_points() -> dict:
    """
    Generate coordinates for 16 points of the screen, dividing the screen
     into fourths, shown as X's below

        X - - X - - X - - X
        |                 |
        |                 |
        X     X     X     X
        |                 |
        |                 |
        X     X     X     X
        |                 |
        |                 |
        X - - X - - X - - X

        returns the coordinates as a dict

    """
    # Get screen resolution
    user32 = windll.user32
    w = user32.GetSystemMetrics(0)
    h = user32.GetSystemMetrics(1)
    result = {'top':
                  {'left': (0, 0),
                   'mid-left': (w/3, 0),
                   'mid-right': (2*w/3, 0),
                   'right': (w, 0)},
              'mid-top':
                  {'left': (0, h/3),
                   'mid-left': (w/3, h/3),
                   'mid-right': (2*w/3, h/3),
                   'right': (w, h/3)},
              'mid-bottom':
                  {'left': (0, 2*h/3),
                   'mid-left': (w/3, 2*h/3),
                   'mid-right': (2*w/3, 2*h/3),
                   'right': (w, 2*h/3)},
              'bottom':
                  {'left': (0, h),
                   'mid-left': (w/3, h),
                   'mid-right': (2*w/3, h),
                   'right': (w, h)}
              }
    return result


def generate_screen_regions(point) -> dict:
    """Returns a dict object of regions used for clicking sections of the screen"""
    result = {'top-outside': Polygon([point['top']['left'], point['top']['right'],
                                      point['mid-bottom']['right'], point['mid-bottom']['mid-right'],
                                      point['mid-top']['mid-right'], point['mid-top']['mid-left'],
                                      point['mid-bottom']['mid-left'], point['mid-bottom']['left']
                                      ]),
              'middle': Polygon([point['mid-top']['left'], point['mid-top']['right'],
                                 point['mid-bottom']['right'], point['mid-bottom']['left']
                                 ])
              }
    return result

# ==============================================================
# Make settings variable available for import
# ==============================================================
SETTINGS = import_config_settings()
# Add screen coordinates
SETTINGS['points'] = generate_screen_points()
SETTINGS['regions'] = generate_screen_regions(SETTINGS['points'])
