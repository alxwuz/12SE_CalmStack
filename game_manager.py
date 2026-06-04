class GameManager:
    def __init__(self):
        self.currentScore = 0
        self.highScore = 0
        self.isGameOver = False

    def startGame(self):
        self.currentScore = 0
        self.isGameOver = False
        print("game has started.") # confirmation in terminal to verify execution

    def updateScore(self):
        pass

    def checkGameOver(self):
        pass