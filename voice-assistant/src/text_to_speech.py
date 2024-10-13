from ENV_VAR import path_to_config
from gtts import gTTS
import pyttsx3
import configparser
import playsound

class Speak:
    def __init__(self, filename='voice.wav'):
        self.filename = filename
        self.config = configparser.ConfigParser()
        self.config.read(path_to_config)
        self.mode = (self.config.get('TTS', 'mode', fallback='pyttsx3'))
        self.engine = None
        
        if self.mode != "gTTS":
            self.engine = pyttsx3.init() 
            
    def speak(self, text):
        try:
            if self.mode == "gTTS":
                tts = gTTS(text=text, lang='en')
                tts.save(self.filename)
                playsound.playsound(self.filename)
                  
            else:
                self.engine.say(text)
                self.engine.runAndWait()
                
        except Exception as e:
            print(f"Error in speech synthesis: {e}")