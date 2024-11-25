class Character:
    def __init__(self):
        self.currentCharacter = "hangman"
        
    def setCharacter(self, characterName):
        self.currentCharacter = characterName
        
    def stageAttempts(self, attempts):
        stages = {
           6: 0,
           5: 1,
           4: 2,
           3: 3,
           2: 4,
           1: 5,
           0: 6
       }
        stage = stages.get(attempts, 6)
        
        if self.currentCharacter == "robot":
            self.robot(stage)
        elif self.currentCharacter == "pirate":
            self.pirate(stage)
        else:
            self.hangman(stage)
        
    def hangman(self, stage):
        hangmanStages = [
            "+---+\n    |\n    |\n    |\n  ===",
            "+---+\n O  |\n    |\n    |\n  ===",
            "+---+\n O  |\n |  |\n    |\n  ===",
            "+---+\n O  |\n/|  |\n    |\n  ===",
            "+---+\n O  |\n/|\\ |\n    |\n  ===",
            "+---+\n O  |\n/|\\ |\n/   |\n  ===",
            "+---+\n O  |\n/|\\ |\n/ \\ |\n  ==="
        ]
        print(hangmanStages[stage])
        
    def robot(self, stage):
        robotStages = [
            "+---+\n      |\n      |\n      |\n   ===",  
            "+---+\n [O]  |\n      |\n      |\n   ===",   
            "+---+\n [O]  |\n  |   |\n      |\n   ===",   
            "+---+\n [O]  |\n /|   |\n      |\n   ===",  
            "+---+\n [O]  |\n /|\\  |\n      |\n   ===",
            "+---+\n [O]  |\n /|\\  |\n /    |\n   ===",  
            "+---+\n [O]  |\n /|\\  |\n / \\  |\n   ==="  
        ]
        print(robotStages[stage])
        
    def pirate(self, stage):
        pirateStages = [
        "+---+\n     |\n     |\n     |\n   ===",    # 0: Empty
        "+---+\n (O) |\n     |\n     |\n   ===",    # 1: Head
        "+---+\n (O) |\n  |  |\n     |\n   ===",    # 2: Body
        "+---+\n (O) |\n <|  |\n     |\n   ===",    # 3: One arm
        "+---+\n (O) |\n <|> |\n     |\n   ===",    # 4: Both arms
        "+---+\n (O) |\n <|> |\n /   |\n   ===",    # 5: One leg
        "+---+\n (O) |\n <|> |\n / \\ |\n   ==="     # 6: Both legs
    ]
        print(pirateStages[stage])

