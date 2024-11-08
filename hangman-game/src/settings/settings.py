from utils.words import getRandomWord
from utils.alerts import Alerts
from utils.clr_console import clr_console, presstoCont
import random

class GameSettings:
    def __init__(self):
        self.originalWord = getRandomWord()
        self.alerts = Alerts()
    
    def showSettings(self):
        clr_console()
        self.alerts.title("Options")
        print("[C]haracter\n[A]bout\nGo [B]ack")
            
        choice = input("\n> ").lower()
    
        if choice == 'c':
            pass # Not implemented Yets
        elif choice == 'a':
            self.about()
        elif choice == 'b':
            return 
        else:
            print("Invalid choice. Returning to main menu.")
            presstoCont()
            return
         
    def about(self):
        clr_console()
        self.alerts.title("About")
        print("Made With \U0001F634")
        input("")