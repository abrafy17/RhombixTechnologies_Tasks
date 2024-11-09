from utils.alerts import Alerts
from utils.clr_console import clr_console, presstoCont
import socket

class GameSettings:
    def __init__(self):
        self.alerts = Alerts()
    
    def isOnline(self):
        try:
            print("Checking Your Internet Connection...")
            socket.create_connection(("8.8.8.8", 53), timeout=2)
            status = True
        
        except OSError:
            status = False
        
    def showSettings(self):
        clr_console()
        self.alerts.title("Options")
        print(f"[C]haracter\n[A]bout\nGo [B]ack")
            
        choice = input("\n> ").lower()
    
        if choice == 'c':
            pass # Not Implemented Yet
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