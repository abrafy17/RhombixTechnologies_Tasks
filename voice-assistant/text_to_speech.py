from gtts import gTTS
import playsound

class Speak:
    def __init__(self, filename='voice.mp3'):
        self.filename = filename
        
    def speak(self, text):
        tts = gTTS(text=text, lang='en')
        tts.save(self.filename)
        playsound.playsound(self.filename)