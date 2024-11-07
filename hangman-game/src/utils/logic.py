from utils.globalVariable import originalWord
from utils.clr_console import clr_console, presstoCont
from utils.alerts import Alerts
from utils.character import Hangman
from settings.settings import GameSettings
import random
import time

game_settings = GameSettings()
hangman = Hangman()
alerts = Alerts()

def replaceLetters(word, num_replacements):
    wordToList = list(word)
    charToReplace = random.sample(range(len(word)), num_replacements)

    for i in charToReplace:
        wordToList[i] = "_"

    return ''.join(wordToList)  

def maskedWord(): # Shows only one time at start of the game
    hiddenWord = replaceLetters(originalWord, game_settings.difficulty())
    return hiddenWord
    
def playGame():
    hiddenWord = maskedWord()
    attempts = 6
    currentWord = hiddenWord

    while attempts > 0:
        clr_console()
        alerts.title("Hangman")
        hangman.stageAttemps(attempts)
        print(f"Try guessing the Word\n{currentWord}")
        userGuess = input("Enter a letter or guess the entire word: ").lower()
        
        if userGuess == originalWord.lower():
            print(f"Congratulations! You've guessed the word: {originalWord}")
            input("Press Any Key to go Back to Main Menu")
            break
        
        elif len(userGuess) == 1:
            if userGuess in originalWord.lower() and userGuess not in currentWord.lower():
                currentWord = ''.join(
                    [originalWord[i] if originalWord[i].lower() == userGuess else currentWord[i] for i in range(len(originalWord))]
                )
                print("Good Guess!")
                time.sleep(2)
                
                if currentWord.lower() == originalWord.lower():
                    print("Well done! You've completed the word:", originalWord)
                    input("Press Any Key to go Back to Main Menu")
                    break
            else:
                print("Letter already revealed or not in the word.")
                attempts -= 1
                time.sleep(1)
        else:
            print("Invalid input. Please guess a single letter or the entire word.")
            time.sleep(2)

        if attempts == 0:
            clr_console()
            alerts.title("Game Over")
            hangman.stageAttemps(attempts)
            print(f"The correct word was: {originalWord}")
            presstoCont()
