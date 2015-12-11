from copy import copy
from marksEnum import Marks
from minimax import Minimax

class Computer():
    def isFree(self, board, i):
        return board[i] == Marks.empty

    def setMarkBoard(self, board, mark, i):
        board[i] = mark
        return board

    def setMark(self, mark):
        self.mark = mark

    def bestMove(self, board):
        self.minimax = Minimax()
        bestMove = 0
        bestValue = -100

        for i in range(len(board)):
            if self.isFree(board, i):
                boardCopy = copy(board)
                boardCopy = self.setMarkBoard(boardCopy, self.mark, i)
                value = self.minimax.minimax(Marks.nought, boardCopy)
                print value

                if value > bestValue:
                    bestMove = i
                    bestValue = value

        return bestMove
