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
