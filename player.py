from gamePolicy import GamePolicy


class Player:
    def __init__(self, mark):
        self.gamePolicy = GamePolicy()
        self.mark = mark

    def getMove(self, board):
        raise NotImplementedError()
