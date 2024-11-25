from utils.alerts import Alerts
from utils.clr_console import clr_console
from utils.character import Character
import socket
import time

class GameSettings:
    def __init__(self):
        self.alerts = Alerts()
        self.currentCharacter = "hangman"
    
    def isOnline(self):
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=2)
            return True
        
        except OSError:
            return False
        
    def selectedCharc(self):
        while True:
            clr_console()
            self.alerts.title("Select Character")
            
            print(f"Current character: {self.currentCharacter.title()}")
            print("Preview")
            tempChar = Character()
            tempChar.setCharacter(self.currentCharacter)
            tempChar.stageAttempts(0)
            
            
            print(f"[H]angman\n[R]obot\n[P]irate\nGo [B]ack")
            
            choice = input("\n> ").lower()
        
            if choice == 'h':
                self.currentCharacter = "hangman"
                print("Character set to Hangman!")
                time.sleep(1)
                return self.currentCharacter
            elif choice == 'r':
                self.currentCharacter = "robot"
                print("Character set to Robot!")
                time.sleep(1)
                return self.currentCharacter
            elif choice == 'p':
                self.currentCharacter = "pirate"
                print("Character set to Pirate!")
                time.sleep(1)
                return self.currentCharacter
            elif choice == 'b':
                return self.currentCharacter
            else:
                print("Invalid Choice, Try Again")
                time.sleep(1)
        
    def showSettings(self):
        while True:
            clr_console()
            self.alerts.title("Options")
            print(f"[C]haracter\n[A]bout\nGo [B]ack")
                
            choice = input("\n> ").lower()
        
            if choice == 'c':
                self.selectedCharc()
            elif choice == 'a':
                self.about()
            elif choice == 'b':
                return 
            else:
                print("Invalid choice. Returning to main menu.")
                time.sleep(1)
                return
    
    def about(self):
        clr_console()
        self.alerts.title("About")
        print("Made With \U0001F634")
        input("")
        
    def getCurrentCharacter(self):
        return self.currentCharacter