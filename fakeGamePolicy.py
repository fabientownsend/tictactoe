class FakeGamePolicy:
    def __init__(self):
        self.responseWin = False
        self.responseCheckTie = False

    def isFree(self, board, i):
        return True

    def win(self, mark, board):
        return self.responseWin

    def checkTie(self, board):
        return self.responseCheckTie
