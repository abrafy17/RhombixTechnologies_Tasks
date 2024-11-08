from utils.alerts import Alerts
from settings.settings import GameSettings
from utils.logic import Game
from utils.clr_console import clr_console
import sys

alerts = Alerts()
game_settings = GameSettings()
game = Game()

def newGame():
    game.playGame()

def main():
    while True:
        clr_console()
        alerts.title("Hangman")
        print(f"Start [N]ew Game\n[O]ptions\n[E]xit to Desktop")
        userChoice = input("\n> ").lower()
        
        if userChoice == 'n':
            newGame()
        elif userChoice == 'o':
            game_settings.showSettings()
        elif userChoice == 'e':
            sys.exit()
        else:
            pass
    
if __name__ == "__main__":
    try:
        main()
        
    except KeyboardInterrupt:
        print("\nForcefully Quit by User")