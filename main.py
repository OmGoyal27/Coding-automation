from appopener import open_app
from webopener import visit
from extracter import load_apps, load_websites  

def perform():                      # The main thing
    apps = load_apps()              # Stores the list of apps into a variable
    websites = load_websites()      # Stores the list of websites into a variable
    for app in apps:
        open_app(app)               # Opens each app individually
    visit(websites)                 # Visits all the websites

perform()                           # Calls the main thing (You can make this be called when something happens)