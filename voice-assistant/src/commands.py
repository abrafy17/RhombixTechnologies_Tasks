import speech_recognition as sr
import os
from sys import exit
from src.search_engine import Query
from src.player_control import MediaController
from src.text_to_speech import Speak
from src.time_date import TimeDate
from src.applications import Applications
from src.weather import Weather
from src.names import Names
from src.roll_a_dice import Roll
from src.music import Play

class Commands():
    def __init__(self):
        self.speaker = Speak()
        self.media_controller = MediaController()
        self.query = Query()
        self.names = Names()
        self.apps = Applications()
        self.time_date = TimeDate()
        self.weather = Weather()
        self.roll = Roll()
        self.play = Play()
        
    def clr_scr(self):
        if os.name == 'nt':
            os.system("cls")
        else: 
            os.system("clear")
    
    def get_audio(self):
        speech = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = speech.listen(source)
            said = ""
            
            try:
                said = speech.recognize_google(audio)
                print(f"You said: {said}")
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
                self.speaker.speak("Sorry, I could not understand the audio.")
                return ""
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                self.speaker.speak("There was an issue with the speech service.")
                return ""
            except Exception as e:
                print("Exception: " + str(e))
                return ""
                
        return said.lower() 

    def parse_commands(self, command):
        if "my name" in command and "change" not in command:
            print(f"Your name is {self.names.user_name()}")
            self.speaker.speak(f"Your name is {self.names.user_name()}")
                        
        elif "your name" in command and "change" not in command:
            print(f"Your name is {self.names.assistant_name()}")
            self.speaker.speak(f"My Name is {self.names.assistant_name()}")
                        
        elif "change my name" in command:
            self.names.change_user_name()
                        
        elif "change your name" in command:
            self.names.change_bot_name()
                        
        elif "resume" in command or "pause" in command:
            self.media_controller.play_pause()
                        
        elif "next track" in command:
                self.media_controller.next_track()
                        
        elif "previous track" in command:
            self.media_controller.previous_track()
            
        elif "play" in command or "music" in command:
            self.play.Music(command)
            
        elif "roll a dice" in command:
            self.roll.dice()
            
        elif "flip a coin" in command:
            self.roll.coin()
            
        elif "choose between" in command:
            self.roll.choice(command)
                        
        elif "time" in command:
            self.time_date.get_time()
                    
        elif "date" in command:
            self.time_date.get_date()

        elif "search" in command:
            if "youtube" in command:
                self.query.search(command, 'youtube')
                    
            elif "wikipedia" in command:
                self.query.search(command, 'wikipedia')
                    
            else:
                self.query.search(command, 'google')
                    
        elif "open" in command:
            app_name = command.replace("open", "").strip()
            self.apps.get_app(app_name)
            
        elif "weather" in command:
            self.weather.get_weather(command)
                    
        elif " quit" in command or "exit" in command:
            self.speaker.speak(f"Goodbye {self.names.user_name()}")
            exit()
        
        else:
            self.speaker.speak("Can't help with this right now")
            print("Can't help with this right now")
    
    def commands(self):
        if self.names.user_name() == None:
                self.names.empty_user_name()
        while True:
            command = self.get_audio()
            if command:
                self.parse_commands(command)
                self.clr_scr()