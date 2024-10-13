from src.text_to_speech import Speak
import datetime

class TimeDate():
    def __init__(self):
        self.now = datetime.datetime.now()
        self.speaker = Speak()
        
    def get_time(self):
        current_time = self.now.strftime("%H:%M %p")
        self.speaker.speak(f"The current time is {current_time}")
        print(current_time)
    
    def get_date(self):
        current_date = self.now.strftime("%d %B %Y")
        self.speaker.speak(f"Today's date is {current_date}")
        print(current_date)