import speech_recognition as sr
import webbrowser 
import datetime
import subprocess
from conn import get_user_name, get_assistant_name, add_names, setup_database
from player_control import MediaController
from text_to_speech import Speak

conn = setup_database()
user_name = get_user_name(conn)
bot_name = get_assistant_name(conn)

speaker = Speak()
media_controller = MediaController()

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
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print("Exception: " + str(e))
            
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

if __name__ == "__main__":
    if not user_name:
        speaker.speak("Welcome for the First time, What is your name?")
        user_name = input("Enter Your Name\n> ")
        speaker.speak("What would you like to call me?")
        bot_name = input("Enter the Assistant Name\n> ")
        speaker.speak(f"Hey {user_name} you set my name to {bot_name}")
        add_names(conn, user_name, bot_name)
        
    speaker.speak(f"Hello {user_name}, How can I help you?")
    
    while True:
        command = get_audio()

        if "my name" in command:
            speaker.speak(f"Your name is {user_name}")
            
        if "your name" in command:
            speaker.speak(f"My Name is {bot_name}")
            
        if "play" in command or "pasue" in command:
            media_controller.play_pause()
            
        if "next track" in command:
            media_controller.next_track()
            
        if "previous track" in command:
            media_controller.previous_track()
            
        if "time" in command:
            get_time()
        
        if "date" in command:
            get_date()

        if "search" in command:
            if "youtube" in command:
                search(command, 'youtube')
            else:
                search(command, 'google')
        
        if "open" in command:
            app_name = command.replace("open", "").strip()
            get_app(app_name)
            
        if "quit" in command or "exit" in command:
            speaker.speak(f"Goodbye {user_name}")
            exit()


conn.close()
