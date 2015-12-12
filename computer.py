import random
from copy import copy
from marksEnum import Marks
from minimax import Minimax

class Computer():
    def __init__(self, idPlayer):
        self.idPlayer = idPlayer

    def isFree(self, board, i):
        return board[i] == Marks.empty

    def setMarkBoard(self, board, mark, i):
        board[i] = mark
        return board

    def setMark(self, mark):
        self.mark = mark

    def isEmpty(self, board):
        for i in board:
            if i != Marks.empty:
                return False

        return True

    def bestMove(self, board):
        if self.isEmpty(board):
            startMoves = [0, 2, 4, 6, 8]
            return random.choice(startMoves)

        self.minimax = Minimax()
        bestMove = 0
        bestValue = -100

        for i in range(len(board)):
            if self.isFree(board, i):
                boardCopy = copy(board)
                boardCopy = self.setMarkBoard(boardCopy, self.mark, i)
                value = self.minimax.minimax(Marks.nought, boardCopy)

                if value > bestValue:
                    bestMove = i
                    bestValue = value

        return bestMove
