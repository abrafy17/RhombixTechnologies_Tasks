import os

def clr_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def presstoCont():
    input("Press any key to contine...")