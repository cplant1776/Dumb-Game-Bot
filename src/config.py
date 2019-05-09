# Standard Library Imports
# Third Party Imports
from os.path import abspath
from yaml import FullLoader, load
# Local Imports


# ==============================================================
# Import Settings From config.yaml
# ==============================================================
def convert_config_paths(config):
    """Convert paths from yaml config to local OS format"""
    for branch in config['img_paths'].values():
        for k, v in branch.items():
            branch[k] = abspath(v)


def import_config_settings() -> dict:
    """Import yaml file as dictionary"""
    with open('config.yaml', 'r') as f:
        result = load(f, Loader=FullLoader)
        convert_config_paths(result)
    return result


# ==============================================================
# Make settings variable available for import
# ==============================================================
SETTINGS = import_config_settings()
