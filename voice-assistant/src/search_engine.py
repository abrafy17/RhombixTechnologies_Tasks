from src.text_to_speech import Speak
import webbrowser
import wikipedia

class Query:
    def __init__(self):
        self.speaker = Speak()
        
    def search(self, command, platform):
        command = command.replace('search', '').replace('for', '').strip()
        
        if platform == 'google':
            query = command.replace('google', '').strip()
            command = query.replace(' ', '+')
            url = f"https://www.google.com/search?q={command}"
            webbrowser.open(url)
            self.speaker.speak(f"Searching {query} on Google.")
            print(f"Searching {query} on Google.")
            
        elif platform == 'youtube':
            query = command.replace('youtube', '').strip()
            command = query.replace(' ', '+')
            url = f"https://www.youtube.com/results?search_query={command}"
            webbrowser.open(url)
            self.speaker.speak(f"Searching {query} on YouTube.")
            print(f"Searching {query} on YouTube.")
            
        elif platform =='wikipedia':
            query = command.replace('wikipedia', '').strip()
            self.speaker.speak(f"Searching WikiPedia for {query}")
            print(f"Searching WikiPedia for {query}")
            result = wikipedia.summary(query, sentences=1)
            self.speaker.speak(result)
            print(result)
            