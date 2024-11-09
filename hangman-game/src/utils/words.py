from settings.settings import GameSettings
import random
import json


class Words:
    def __init__(self):
        self.status = GameSettings()
    
    def getRandomWord(self):
        if self.status.isOnline:
            return self.onlineWords()
        else:
            return self.offlineWords()
        
    def onlineWords(self): # Call API for Word
        return "online"
    
    def offlineWords(self):
        with open("src/data/words.json", "r") as file:
            data = json.load(file)
            wordsList = data["words"]
        return random.choice(wordsList)
