from utils.clr_console import clr_console, presstoCont
from utils.words import getRandomWord
from utils.alerts import Alerts
from utils.character import Hangman
from settings.settings import GameSettings
import random
import json
import time


class GameLogic():
    def __init__(self):
        self.game_settings = GameSettings()
        self.hangman = Hangman()
        self.alerts = Alerts()

    def replaceLetters(self, word, num_replacements):
        wordToList = list(word)
        charToReplace = random.sample(range(len(word)), num_replacements)

        for i in charToReplace:
            wordToList[i] = "_"

        return ''.join(wordToList)  

    def maskedWord(self):
        hiddenWord = self.replaceLetters(self.originalWord, self.game_settings.difficulty())
        return hiddenWord
        
    def playGame(self):
        self.originalWord = getRandomWord()
        hiddenWord = self.maskedWord()
        attempts = 6
        currentWord = hiddenWord
        guessed_letters = set()

        while attempts > 0:
            clr_console()
            self.alerts.title("Hangman")
            self.hangman.stageAttemps(attempts)
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
                self.hangman.stageAttemps(attempts)
                print(f"The correct word was: {self.originalWord}")
                presstoCont()
