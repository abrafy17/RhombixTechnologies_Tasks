import subprocess
from src.text_to_speech import Speak

class Applications():
    def __init__(self):
        self.speaker = Speak()
        
    def get_app(self, app_name):
        app_commands = {
            "browser": "firefox",  
            "terminal": "kitty",  
            "text editor": "code", 
            "player": "vlc"  
        }
        
        if app_name in app_commands:
            subprocess.Popen([app_commands[app_name]])
            print(f"Opening {app_name}.")
            self.speaker.speak(f"Opening {app_name}")
        else:
            print("Application not recognized.")