import configparser
import requests
from src.text_to_speech import Speak
from ENV_VAR import path_to_config

class Weather():
    def __init__(self):
        self.speaker = Speak()
        config = configparser.ConfigParser()
        config.read(path_to_config)
        self.token = config['API_KEYS']['weather_api']
    
    def get_weather(self, command):
        command = command.replace('current', '').replace('weather', '').replace('in', '').strip()
        command = command.replace(' ', '+')
        city = command
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.token}"
        print(f"Looking up the weather of {city}")
        res = requests.get(url)
        weather = res.json()
        
        if weather.get("cod") == 401:
            self.speaker.speak("Invalid API key. Please check your API key.")
            print("Error! Invalid API key.")
            return None
                
        if res.status_code == 404:
            self.speaker.speak(f"Sorry, Can't find the city named {city}")
            print(f"Error! Status code: {res.status_code}, {city} not found")
            return None
        
        if res.status_code != 200:
            self.speaker.speak("Sorry, I couldn't fetch the weather data.")
            print(f"Error! Status code: {res.status_code}, Response: {res.json()}")
            return None
        
        weather = res.json()
        tempurature = weather['main']['temp'] - 273.15
        description = weather['weather'] [0] ['description']
        city = weather["name"]
        country = weather['sys']['country']
        
        self.speaker.speak(f"Current weather at {city} {country} is {tempurature:.1f}degrees celsius with {description}")
        print(f"Current weather at {city} {country} is {tempurature:.1f}degrees Celsius with {description}")