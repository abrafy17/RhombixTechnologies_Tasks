import os

def clr_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def presstoCont():
    input("\nPress any key to contine...")