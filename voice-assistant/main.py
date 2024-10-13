from src.commands import Commands
from src.text_to_speech import Speak

if __name__ == "__main__":
    command = Commands()
    speaker = Speak()
    print("Hello Welcome to Voice Assistant")
    speaker.speak("Hello Welcome to Voice Assistant")
    try:
        command.commands()
    except KeyboardInterrupt:
        print("\nProgram closed by User.")