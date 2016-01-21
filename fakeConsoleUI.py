class FakeConsoleUI:
    def __init__(self):
        self.passedIntoDisplayTie = False
        self.passedIntoDisplayWinner = False

    def getPlayerMove(self):
        return 4

    def typeGameSelected(self):
        return 2

    def getFirstPlayer(self):
        return 1

    def displayTypeGame(self):
        return None

    def displayWhichStart(self):
        return None

    def displayTie(self):
        self.passedIntoDisplayTie = True
        return None

    def displayWinner(self, value):
        self.passedIntoDisplayWinner = True
        return None

    def displayPlayerTurn(self, mark):
        return None

    def displayBoard(self, board):
        return None
