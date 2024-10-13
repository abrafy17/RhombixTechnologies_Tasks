from src.text_to_speech import Speak
import random

class Roll():
    def __init__(self):
        self.speaker = Speak()
        
    def dice(self):
        result = random.randint(1, 6)
        rolled = f"Rolled Number is {result}"
        self.speaker.speak(rolled)