import speech_recognition as sr
import webbrowser 
import datetime
import os
import subprocess
from conn import get_user_name, get_assistant_name, add_names, setup_database
from player_control import MediaController
from text_to_speech import Speak

conn = setup_database()
user_name = get_user_name(conn)
bot_name = get_assistant_name(conn)
if bot_name:
    bot_name = bot_name[0] 
else:
    bot_name = "Assistant"
print(f"Hello My Name is {bot_name}, Say 'Hey {bot_name}' for Assistance :)")

speaker = Speak()
media_controller = MediaController()

def clr_scr():
    if os.name == 'nt':
        os.system("cls")
    else: 
        os.system("clear")

def get_audio():
    speech = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = speech.listen(source)
        said = ""
        
        try:
            said = speech.recognize_google(audio)
            print(f"You said: {said}")
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""
        except Exception as e:
            print("Exception: " + str(e))
            return ""
            
    return said.lower()  

def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M %p")
    speaker.speak(f"The current time is {current_time}")
    print(current_time)
    
def get_date():
    now = datetime.datetime.now()
    current_date = now.strftime("%d %B %Y")
    speaker.speak(f"Today's date is {current_date}")
    print(current_date)

def search(command, platform):
    command = command.replace('search', '').strip()
    if not command:
        speaker.speak("Please try again...")
        print("Invalid command.")
        return

    if platform == 'google':
        query = command
        command = command.replace(' ', '+')
        url = f"https://www.google.com/search?q={command}"
        webbrowser.open(url)
        speaker.speak(f"Searching {query} on Google.")
        print(f"Searching {command} on Google.")
        
    elif platform == 'youtube':
        query = command
        command = command.replace(' ', '+')
        url = f"https://www.youtube.com/results?search_query={command}"
        webbrowser.open(url)
        speaker.speak(f"Searching {query} on YouTube.")
        print(f"Searching {command} on YouTube.")

def get_app(app_name):
    app_commands = {
        "browser": "firefox",  
        "terminal": "kitty",  
        "text editor": "code", 
        "vlc": "vlc"  
    }
    
    if app_name in app_commands:
        subprocess.Popen([app_commands[app_name]])
        speaker.speak(f"Opening {app_name}")
        print(f"Opening {app_name}.")
    else:
        print("Application not recognized.")

def change_user_name(conn, bot_name):
    speaker.speak("What would you like me to call you?")
    new_user_name = input("Enter You Name:\n> ")
    add_names(conn, new_user_name, bot_name)
    print(f"User name is set to {new_user_name}")
    return new_user_name
    
def change_bot_name(conn, user_name):
    speaker.speak("What you want to call me?")
    new_bot_name = input("Enter New Name:\n> ")
    add_names(conn, user_name, new_bot_name)
    print(f"Assistant name is changed to {new_bot_name}")
    return new_bot_name
    
if __name__ == "__main__":
    if not user_name:
        speaker.speak("Welcome for the First time, What is your name?")
        user_name = input("Enter Your Name\n> ")
        speaker.speak("What would you like to call me?")
        bot_name = input("Enter the Assistant Name\n> ")
        speaker.speak(f"Hey {user_name} you set my name to {bot_name}")
        add_names(conn, user_name, bot_name)
        
    
    while True:
        clr_scr()
        print("Standing By...")
        command = get_audio()
        
        if command:
            WAKE_STR = ["hey", "hello", "hi", "listen", "wake up", bot_name]
            if any(wake in command for wake in WAKE_STR):
                speaker.speak(f"I am listening")
                command = get_audio()
                
                if "my name" in command and "change" not in command:
                    speaker.speak(f"Your name is {user_name}")
                    
                elif "your name" in command and "change" not in command:
                    speaker.speak(f"My Name is {bot_name}")
                    
                elif "change my name" in command:
                    user_name = change_user_name(conn, bot_name)
                    
                elif "change your name" in command:
                    bot_name = change_bot_name(conn, user_name)
                    
                elif "play" in command or "pause" in command:
                    media_controller.play_pause()
                    
                elif "next track" in command:
                    media_controller.next_track()
                    
                elif "previous track" in command:
                    media_controller.previous_track()
                    
                elif "time" in command:
                    get_time()
                
                elif "date" in command:
                    get_date()

                elif "search" in command:
                    if "youtube" in command:
                        search(command, 'youtube')
                    else:
                        search(command, 'google')
                
                elif "open" in command:
                    app_name = command.replace("open", "").strip()
                    get_app(app_name)
                
                else:
                    speaker.speak("Can't help with this right now")
                    print("Can't help with this right now")
        else:
            print(f"Say 'hey {bot_name}' for Assistance")
            if "quit" in command or "exit" in command:
                    speaker.speak(f"Goodbye {user_name}")
                    exit()

conn.close()
