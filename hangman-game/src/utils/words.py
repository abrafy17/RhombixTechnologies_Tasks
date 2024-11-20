from settings.settings import GameSettings
import requests
import random
import json

class Words:
    def __init__(self):
        self.status = GameSettings()
    
    def getRandomWord(self):
        if self.status.isOnline:
            try:
                return self.onlineWords()
            except Exception as e:
                print(f"Online word fetch failed: {e}. Using offline words.")
                return self.offlineWords()
        
    def onlineWords(self): # Calls API for Word
        url = 'https://random-word-api.herokuapp.com/word'
        
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            
            word = response.json()
            if word:
                return word[0]
            else:
                raise ValueError("API response is empty")
            
        except (requests.RequestException, ValueError) as e:
            raise Exception(f"Failed to fetch word: {e}")

    def offlineWords(self):
        try:
            with open("src/data/words.json", "r") as file:
                data = json.load(file)
                wordsList = data["words"]
            return random.choice(wordsList)
    
        except FileNotFoundError:
            raise Exception("Offline words file is not found")
       
