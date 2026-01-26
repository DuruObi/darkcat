import os
import yaml

CONFIG_FILE = os.path.expanduser("~/.darkcat.yaml")

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE, "r") as f:
        return yaml.safe_load(f)

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        yaml.dump(config, f)
