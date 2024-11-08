import random
import json

def getRandomWord():
    with open("src/data/words.json", "r") as file:
        data = json.load(file)
        wordsList = data["words"]
    return random.choice(wordsList)
