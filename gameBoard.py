from marksEnum import Marks


class GameBoard():
    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.board = self.createBoard()

    def createBoard(self):
        return [[Marks.empty]*self.boardSize for n in range(self.boardSize)]

    def setMark(self, position, mark):
        row =  position/self.boardSize
        column = position - row*self.boardSize
        self.board[row][column] = mark

    def getMark(self, position):
        row =  position/self.boardSize
        column = position - row*self.boardSize
        return self.board[row][column]

    def isEmpty(self, position):
        return self.getMark(position) == Marks.empty
