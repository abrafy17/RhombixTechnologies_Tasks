from ytmusicapi import YTMusic
from src.text_to_speech import Speak
import os

class Play():
    def __init__(self):
        self.speaker = Speak()
        self.ytmusic = YTMusic("oauth.json") 
    
    def Music(self, command):
        command =   command.replace('play music', '').strip()
        try:
            video_data = self.ytmusic.search(f'{command}')[0]
            url = f"https://www.youtube.com/watch?v={video_data['videoId']}"
            name = video_data['title']
            artist = video_data['artists'][0]['name']
            print(f"Playing {name} by {artist}")
            self.speaker.speak(f"Playing {name} by {artist}")
            os.system(f"kitty mpv --no-video {url}")
            
        except TimeoutError as e:
            print(f"Error {e}")
            self.speaker.speak(f"Error {e}")