import itertools

class FakeGamePolicy:
    def __init__(self):
        self.responseWin = False
        self.responseCheckTie = False
        self.passedInThisMethod = False

    def win(self, mark, board):
        if self.passedInThisMethod:
            return True

        self.passedInThisMethod = True
        return self.responseWin

    def checkTie(self, board):
        return self.responseCheckTie
