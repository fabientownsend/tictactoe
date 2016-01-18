from marksEnum import Marks


class GameBoard():
    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.board = self.createBoard()

    def createBoard(self):
        return [[Marks.empty]*self.boardSize for n in range(self.boardSize)]

    def getBoard(self):
        return self.board

    def setMark(self, position, mark):
        row =  position/self.boardSize
        column = position - row*self.boardSize

        if self.board[row][column] != Marks.empty:
            raise SpotNotEmpty
        else:
            self.board[row][column] = mark

    def getMark(self, position):
        row =  position/self.boardSize
        column = position - row*self.boardSize
        return self.board[row][column]

class SpotNotEmpty(Exception):
    def __init__(self):
        self.msg = 'The spot must be free'
