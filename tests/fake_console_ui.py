class FakeConsoleUI:
    def __init__(self):
        self.passedIntoDisplayTie = False
        self.passedIntoDisplayWinner = False
        self.playerMovePosition = 0
        self.VALIDEPLAYERMOVEPOSITION = 0
        self.passedInThisMethod = False
        self.passedDisplayRangeBoardMethod = False
        self.passedInSpotNotFreeMethod = False

    def getPlayerMove(self):
        if self.passedInThisMethod:
            return self.VALIDEPLAYERMOVEPOSITION

        self.passedInThisMethod = True
        return self.playerMovePosition

    def displayCorrectRangeBoard(self):
        self.passedDisplayRangeBoardMethod = True
        return None

    def spotNotFree(self):
        self.passedInSpotNotFreeMethod = True
        return None

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
