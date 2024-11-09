from settings.settings import GameSettings

class Character:
    def __init__(self):
        self.settings = GameSettings()

    def stageAttempts(self, attempts):
        stages = {
            6: lambda: self.hangman(0),
            5: lambda: self.hangman(1),
            4: lambda: self.hangman(2),
            3: lambda: self.hangman(3),
            2: lambda: self.hangman(4),
            1: lambda: self.hangman(5),
            0: lambda: self.hangman(6),
        }
        
        stage_func = stages.get(attempts, lambda: self.hangman(6))
        stage_func()

    def hangman(self, stage):
        hangmanStages = [
            "+---+\n    |\n    |\n    |\n  ===",
            "+---+\nO   |\n    |\n    |\n  ===",
            "+---+\nO   |\n|   |\n    |\n  ===",
            "+---+\nO   |\n/|  |\n    |\n  ===",
            "+---+\nO   |\n/|\\ |\n    |\n  ===",
            "+---+\nO   |\n/|\\ |\n/   |\n  ===",
            "+---+\nO   |\n/|\\ |\n/ \\ |\n  ==="
        ]
        print(hangmanStages[stage])
