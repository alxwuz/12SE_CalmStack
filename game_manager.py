class GameManager:
    def __init__(self):
        self.currentScore = 0
        self.highScore = 0
        self.isGameOver = False

    def startGame(self):
        self.currentScore = 0
        self.isGameOver = False
        print("Game Started!") # confirmation in terminal to make sure it actually works

    def updateScore(self):
        pass

    def checkGameOver(self):
        pass