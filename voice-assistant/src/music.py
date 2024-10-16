from ytmusicapi import YTMusic
from src.text_to_speech import Speak
from ENV_VAR import path_to_config
import configparser
import os

class Play():
    def __init__(self):
        self.speaker = Speak()
        self.ytmusic = YTMusic("oauth.json") 
        self.config = configparser.ConfigParser()
        self.config.read(path_to_config)
        self.terminal = (self.config.get('TERMINAL', 'emulator', fallback=''))
    
    def Music(self, command):
        command =   command.replace('play music', '').strip()
        try:
            video_data = self.ytmusic.search(f'{command}')[0]
            url = f"https://www.youtube.com/watch?v={video_data['videoId']}"
            name = video_data['title']
            artist = video_data['artists'][0]['name']
            print(f"Playing {name} by {artist}")
            self.speaker.speak(f"Playing {name} by {artist}")
            os.system(f"{self.terminal} mpv --no-video {url}")
            
        except TimeoutError as e:
            print(f"Error {e}")
            self.speaker.speak(f"Error {e}")