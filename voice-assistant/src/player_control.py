import subprocess
from src.text_to_speech import Speak

class MediaController():
    def __init__(self):
        self.speaker = Speak()
        
    def play_pause(self):
        status = subprocess.run(["playerctl", "status"], capture_output=True, text=True)
        if status.stdout.strip() == "Playing":   
            subprocess.run(["playerctl", "pause"])
            print("Pausing")
            self.speaker.speak("Pausing")
        else:
            subprocess.run(["playerctl", "play"])
            print("Playing")
            self.speaker.speak("Playing")
        
    def next_track(self):
        subprocess.run(["playerctl", "next"])
        print("Skipping to next track")
        self.speaker.speak("skipping to next track")
        
    def previous_track(self):
        subprocess.run(["playerctl", "previous"])
        print("Skipping to previous track")
        self.speaker.speak("skipping to previous track")