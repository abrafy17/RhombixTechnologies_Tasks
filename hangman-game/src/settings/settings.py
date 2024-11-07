from utils.globalVariable import originalWord
from utils.alerts import Alerts
from utils.clr_console import clr_console, presstoCont
import random

class GameSettings:
    def __init__(self):
        self.originalWord = originalWord
        self.currentDifficultyLabel = "Random"
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
        print(f"Current Difficulty: {self.displayCurrentDifficulty()}\nSelect Difficulty Level\n[E]asy\n[M]edium\n[H]ard\n[R]andom\nGo [B]ack")
        
        choice = input("\n> ").lower()
        
        if choice == 'e':
            self.currentDifficultyLabel = "Easy"
            self.currentDifficultyReplacements = self.easyDifficulty(self.originalWord)
        elif choice == 'm':
            self.currentDifficultyLabel = "Medium"
            self.currentDifficultyReplacements = self.mediumDifficulty(self.originalWord)
        elif choice == 'h':
            self.currentDifficultyLabel = "Hard"
            self.currentDifficultyReplacements = self.hardDifficulty(self.originalWord)
        elif choice == 'r':
            self.currentDifficultyLabel = "Random"
            self.currentDifficultyReplacements = self.randomDifficulty(self.originalWord)
        elif choice =='b':
            return
        else:
            self.currentDifficultyLabel = "Random"
            self.currentDifficultyReplacements = self.randomDifficulty(self.originalWord)
            print("Invalid difficulty... Set 'Random' as Default")
            presstoCont()
            
        return self.currentDifficultyReplacements
    
    def displayCurrentDifficulty(self):
        return self.currentDifficultyLabel
    
    def about(self):
        clr_console()
        self.alerts.title("About")
        print("Made With \U0001F634")
        input("")