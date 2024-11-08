from utils.alerts import Alerts
from settings.settings import GameSettings
from utils.logic import GameLogic
from utils.clr_console import clr_console, presstoCont

import sys

alerts = Alerts()
game_settings = GameSettings()
game = GameLogic()

def newGame():
    game.playGame()

def showSettings():
    clr_console()
    alerts.title("Settings")
    print("[C]haracter\n[A]bout\nGo [B]ack")
        
    choice = input("\n> ").lower()
   
    if choice == 'c':
        pass # Not implemented Yets
    elif choice == 'a':
        game_settings.about()
    elif choice == 'b':
        return 
    else:
        print("Invalid choice. Returning to main menu.")
        presstoCont()
        return
        
def main():
    while True:
        clr_console()
        alerts.title("Hangman")
        print(f"Start [N]ew Game\n[S]ettings\n[E]xit to Desktop")
        userChoice = input("\n> ").lower()
        
        if userChoice == 'n':
            newGame()
        elif userChoice == 's':
            showSettings()
        elif userChoice == 'e':
            sys.exit()
        else:
            pass
    
if __name__ == "__main__":
    try:
        main()
        
    except KeyboardInterrupt:
        print("\nForcefully Quit by User")