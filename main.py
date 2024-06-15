from pathlib import Path
import json
import webbrowser
import os
import subprocess

def open_app(path):                                             # Opens the app
    if os.path.exists(path):
        print(f"The file exists at: {path}")
        try:
            # Run the executable with quotes to handle spaces
            subprocess.run([path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error occurred: {e}")
    else:
        print("The file does not exist.")

def visit(urls):                # Opens all of the urls
    for url in urls:
        webbrowser.open(url)

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

def main():                      # The main thing
    apps = load_apps()              # Stores the list of apps into a variable
    websites = load_websites()      # Stores the list of websites into a variable
    for app in apps:
        open_app(app)               # Opens each app individually
    visit(websites)                 # Visits all the websites

main()                           # Calls the main thing (You can make this be called when something happens)