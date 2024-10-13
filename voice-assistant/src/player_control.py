import subprocess
from src.text_to_speech import Speak

class MediaController():
    def __init__(self):
        self.speaker = Speak()
        
    def play_pause(self):
        status = subprocess.run(["playerctl", "status"], capture_output=True, text=True)
        if status.stdout.strip() == "Playing":   
            subprocess.run(["playerctl", "pause"])
            self.speaker.speak("Pausing")
            print("Pausing")
        else:
            subprocess.run(["playerctl", "play"])
            self.speaker.speak("Playing")
            print("Playing")
        
    def next_track(self):
        subprocess.run(["playerctl", "next"])
        self.speaker.speak("skipping to next track")
        print("Skipping to next track")
        
    def previous_track(self):
        subprocess.run(["playerctl", "previous"])
        self.speaker.speak("skipping to previous track")
        print("Skipping to previous track")