from utils.globalVariable import originalWord
from utils.alerts import Alerts
from utils.clr_console import clr_console
import random

class GameSettings:
    def __init__(self):
        self.originalWord = originalWord
        self.currentDifficultyReplacements = self.randomDifficulty(self.originalWord) 
        self.alerts = Alerts()
          
    def randomDifficulty(self, word):
        numReplacements = random.randint(1, len(word) - 1)
        return numReplacements
    
    def easyDifficulty(self, word):
        wordLen = len(word)
        if wordLen >= 4:  
            return 2
        else:
            return 1
        
    def mediumDifficulty(self, word):
        wordLen = len(word)
        if wordLen >= 4: 
            return 3
        else:
            return 2
        
    def hardDifficulty(self, word):
        wordLen = len(word)
        if wordLen >= 4: 
            return 4
        else:
            return 3

    def difficulty(self):
        clr_console()
        self.alerts.title("Diificulty")
        print(f"Select Difficulty Level\n[E]asy\n[M]edium\n[H]ard\n[R]andom")
        
        choice = input("\n> ").lower()
        
        if choice == 'e':
            self.currentDifficultyReplacements = self.easyDifficulty(self.originalWord)
        elif choice == 'm':
            self.currentDifficultyReplacements = self.mediumDifficulty(self.originalWord)
        elif choice == 'h':
            self.currentDifficultyReplacements = self.hardDifficulty(self.originalWord)
        else:
            self.currentDifficultyReplacements = self.randomDifficulty(self.originalWord)
            
        return self.currentDifficultyReplacements
    
    def about(self):
        clr_console()
        self.alerts.title("About")
        print("Made With \U0001F634")
        input("")