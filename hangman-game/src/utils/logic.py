from utils.clr_console import clr_console, presstoCont
from utils.words import Words
from utils.alerts import Alerts
from utils.character import Character
import random
import time


class Game():
    def __init__(self):
        self.settings = None
        self.character = Character()
        self.alerts = Alerts()
        self.getWord = Words()

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
        self.alerts.title("Difficulty")
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

    def replaceLetters(self, word, num_replacements):
        wordToList = list(word)
        charToReplace = random.sample(range(len(word)), num_replacements)

        for i in charToReplace:
            wordToList[i] = "_"

        return ''.join(wordToList)  

    def maskedWord(self):
        hiddenWord = self.replaceLetters(self.originalWord, self.difficulty())
        return hiddenWord
    
    def setSettings(self, settings):
        self.settings = settings
        
    def playGame(self):
        self.originalWord = self.getWord.getRandomWord()
        if not self.originalWord:
            self.alerts.title("Error")
            print("Error Getting Word!\nPlease Report it to Devs.")
            time.sleep(0.2)
            return
        
        currentChar = self.settings.getCurrentCharacter()
        self.character.setCharacter(currentChar)
        
        hiddenWord = self.maskedWord()
        attempts = 6
        currentWord = hiddenWord
        guessed_letters = set()

        while attempts > 0:
            clr_console()
            self.alerts.title("Hangman")
            self.character.stageAttempts(attempts)
            print(f"Attempts Remaining: {attempts}\nTry guessing the Word\n>>> {currentWord}")
            userGuess = input("Enter a letter or guess the entire word: ").lower()
            
            if userGuess == self.originalWord.lower():
                clr_console()
                self.alerts.title("Hurray!")
                print(f"You've guessed the word: {self.originalWord}")
                input("\n")
                break
            
            elif len(userGuess) == 1:
                if userGuess in self.originalWord.lower() and userGuess not in guessed_letters:
                    guessed_letters.add(userGuess)
                    currentWord = ''.join(
                        [self.originalWord[i] if self.originalWord[i].lower() in guessed_letters else currentWord[i] for i in range(len(self.originalWord))]
                    )
                    print("Good Guess!")
                    time.sleep(1)
                    
                    if currentWord.lower() == self.originalWord.lower():
                        clr_console()
                        self.alerts.title("Hurray!")
                        print(f"You've completed the word: {self.originalWord}")
                        input("Press any key to go back to main menu.\n")
                        break
                else:
                    print("Letter already revealed or not in the word.")
                    attempts -= 1
                    time.sleep(1)
            else:
                print("Oops! Wrong guess or invalid input.")
                attempts -= 1
                time.sleep(1)

            if attempts == 0:
                clr_console()
                self.alerts.title("Game Over")
                self.character.stageAttempts(attempts)
                print(f"The correct word was: {self.originalWord}")
                presstoCont()
