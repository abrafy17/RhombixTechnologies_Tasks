from src.text_to_speech import Speak
import datetime

class TimeDate():
    def __init__(self):
        self.now = datetime.datetime.now()
        self.speaker = Speak()
        
    def get_time(self):
        current_time = self.now.strftime("%H:%M %p")
        print(current_time)
        self.speaker.speak(f"The current time is {current_time}")
    
    def get_date(self):
        current_date = self.now.strftime("%d %B %Y")
        print(current_date)
        self.speaker.speak(f"Today's date is {current_date}")