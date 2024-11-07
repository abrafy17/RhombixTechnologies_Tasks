class Hangman:
    def __init__(self):
        pass
    
    def stageAttemps(self, attempts):
        stages = {
            6: self.stage_start,
            5: self.stage_one,
            4: self.stage_two,
            3: self.stage_three,
            2: self.stage_four,
            1: self.stage_five,
            0: self.stage_dead
        }
        
        stage_func = stages.get(attempts, self.stage_dead)
        stage_func()
        
    def stage_start(self):
        hangman = """
                +---+
                    |
                    |
                    |
                  ===
                  """
        print(hangman)
    
    def stage_one(self):
        hangman = """
                +---+
                O   |
                    |
                    |
                  ===
                  """
        print(hangman)
    
    def stage_two(self):
        hangman = """
                +---+
                O   |
                |   |
                    |
                  ===
                  """
        print(hangman)
    
    def stage_three(self):
        hangman = """
                +---+
                 O  |
                /|  |
                    |
                  ===
                  """
        print(hangman)
    
    def stage_four(self):
        hangman = """
                +---+
                 O  |
                /|\ |
                    |
                  ===
                  """
        print(hangman)
    
    def stage_five(self):
        hangman = """
                +---+
                 O  |
                /|\ |
                /   |
                  ===
                  """
        print(hangman)
    
    def stage_dead(self):
        hangman = """
                +---+
                 O  |
                /|\ |
                / \ |
                  ===
                  """
        print(hangman)