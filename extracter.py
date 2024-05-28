from pathlib import Path
import json

def load_websites():                        # Extracts all the information from the websites.json file
    file_path = Path("websites.json")

    if not file_path.exists():
        return []
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading websites: {e}")
        return []
    
def load_apps():                            # Extracts all the apps
    file_path = Path("apps.json")

    if not file_path.exists():
        return []
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading apps: {e}")
        return []