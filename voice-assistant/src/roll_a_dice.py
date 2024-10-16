from src.text_to_speech import Speak
import random

class Roll():
    def __init__(self):
        self.speaker = Speak()
        
    def dice(self):
        result = random.randint(1, 6)
        print(f"Rolled number is: {result}")
        self.speaker.speak(f"Rolled number is {result}")
        
    def coin(self):
        coinFlip = random.coin(['Heads', 'Tails'])
        print(f" Coin shows {coinFlip}")
        self.speaker.speaks(f"Its {coinFlip}")
        
    def choice(self, command):
        command = command.replace('choose', '').replace('between', '').strip()
        choices = command.split('and')
        if len(choices) >= 2:
            first_choice = choices[0].strip()
            second_choice = choices[1].strip()
            
            choice = random.choice([first_choice, second_choice])
            print(f"I choose {choice}")
            self.speaker.speak(f"I choose {choice}")
            
        else:
            self.speaker.speak(f"There's nothing to choose between")