import json
from pathlib import Path

def load_json():
    # creating the data directory for this project
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    CONFIG_DIR = str(BASE_DIR) + "/config"
    CONFIG_FILE = CONFIG_DIR + "/config_measurements.json"
    # open json configuration file with error check
    try:
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        print("Error: File not found!")
    except json.JSONDecodeError:
        print("Error: Syntax error on JSON file!")
    
    return config
