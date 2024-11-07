from utils.globalVariable import originalWord
from utils.alerts import Alerts
from utils.character import Hangman
from settings.settings import GameSettings
import random

game_settings = GameSettings()
difficulty = game_settings.difficulty()
hangman = Hangman()
alerts = Alerts()


def replaceLetters(word, num_replacements):
    
    wordToList = list(word)
    charToReplace = random.sample(range(len(word)), num_replacements)

    for i in charToReplace:
        wordToList[i] = "_"

    return ''.join(wordToList)  

def maskedWord(): # Shows only one time at start of the game
    global originalWord
    global difficulty
    print(f"Debug: Difficulty is {difficulty}") #testcase
    hiddenWord = replaceLetters(originalWord, difficulty)
    return hiddenWord
    
def playGame():
    hiddenWord = maskedWord()
    attempts = 6
    currentWord = hiddenWord
    
    alerts.title("Hangman")
    print(f"Try guessing the Word\n{currentWord}")
    
    while attempts > 0:
        userGuess = input("Enter a letter or guess the entire word: ").lower()
        
        if userGuess == originalWord.lower():
            print(f"Congratulations! You've guessed the word: {originalWord}")
            break
        
        elif len(userGuess) == 1 and userGuess in originalWord.lower():
            currentWord = ''.join(
                [originalWord[i] if originalWord[i].lower() == userGuess else currentWord[i] for i in range(len(originalWord))]
            )
            print("Good Guess!")
            print("Current word:", currentWord)
            
            if currentWord.lower() == originalWord.lower():
                print("Well done! You've completed the word:", originalWord)
                break
            
            else:
                attempts -= 1
                hangman.stageAttemps(attempts)
                
            if attempts == 0:
                alerts.title("Game Over")
                print(f"The Correct word was: {originalWord}")
'''
Example usage
print(maskedWord)
'''