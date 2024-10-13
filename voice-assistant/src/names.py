from src.conn import Database
from src.text_to_speech import Speak

class Names():
    def __init__(self):
        self.speaker = Speak()
        self.database = Database()
        self.conn = self.database.setup_database()
        
    def user_name(self):
        user_name = self.database.get_user_name(self.conn)
        return user_name[0] if user_name else None
    
    def assistant_name(self):
        bot_name = self.database.get_assistant_name(self.conn)
        return bot_name[0] if bot_name else "Assistant"
        
    def change_user_name(self):
        self.speaker.speak("What would you like me to call you?")
        new_user_name = input("Enter Your Name:\n> ")
        bot_name = self.assistant_name()
        self.database.add_names(self.conn, new_user_name, bot_name)
        self.speaker.speak(f"You name is {new_user_name}")
        print(f"User name is set to {new_user_name}")
        return new_user_name
        
    def change_bot_name(self):
        self.speaker.speak("What you want to call me?")
        new_bot_name = input("Enter New Name:\n> ")
        user_name = self.user_name()
        self.database.add_names(self.conn, user_name, new_bot_name)
        self.speaker.speak(f"You chnaged my name to {new_bot_name}")
        print(f"Assistant name is changed to {new_bot_name}")
        return new_bot_name
    
    def empty_user_name(self):
        self.speaker.speak("Welcome for the First time, What is your name?")
        user_name = input("Enter Your Name\n> ")
        self.speaker.speak("What would you like to call me?")
        bot_name = input("Enter the Assistant Name\n> ")
        self.speaker.speak(f"Hey {user_name} you set my name to {bot_name}")
        self.database.add_names(self.conn, user_name, bot_name)