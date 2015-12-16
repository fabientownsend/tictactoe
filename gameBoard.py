from marksEnum import Marks


class GameBoard():
    def __init__(self):
        self.board = self.createBoard()

    def resetBoard(self):
        self.board = self.createBoard()

    def createBoard(self):
        return [
            Marks.empty, Marks.empty, Marks.empty,
            Marks.empty, Marks.empty, Marks.empty,
            Marks.empty, Marks.empty, Marks.empty
        ]

    def getBoard(self):
        return self.board

    def setMark(self, position, mark):
        if self.board[position] != Marks.empty:
            raise SpotNotEmpty
        else:
            self.board[position] = mark


class SpotNotEmpty(Exception):
    def __init__(self):
        self.msg = 'The spot must be free'
