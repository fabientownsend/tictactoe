from marksEnum import Marks
from copy import copy

class Minimax():
    def checkTie(self, board):
        for i in board:
            if i == Marks.empty:
                return False

        return True

    def win(self, mark, board):
        if (
            (board[0] == mark and board[1] == mark and board[2] == mark) or
            (board[3] == mark and board[4] == mark and board[5] == mark) or
            (board[6] == mark and board[7] == mark and board[8] == mark) or
            (board[0] == mark and board[3] == mark and board[6] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[0] == mark and board[4] == mark and board[8] == mark) or
            (board[2] == mark and board[4] == mark and board[6] == mark)
            ):
            return True
        else:
            return False

    def isFree(self, board, i):
        return board[i] == Marks.empty

    def setMark(self, board, mark, i):
        board[i] = mark
        return board

    def minimax(self, mark, board):
        if self.win(Marks.cross, board):
            return 1
        elif self.win(Marks.nought, board):
            return -1
        elif self.checkTie(board):
            return 0

        if mark == Marks.cross:
            bestValue = -100

            for i in range(len(board)):
                if self.isFree(board, i):
                    boardCopy = copy(board)
                    boardCopy = self.setMark(boardCopy, mark, i)
                    val = self.minimax(Marks.nought, boardCopy)
                    bestValue = max(val, bestValue)

            return bestValue
        else:
            bestValue = 100

            for i in range(len(board)):
                if self.isFree(board, i):
                    boardCopy = copy(board)
                    boardCopy = self.setMark(boardCopy, mark, i)
                    val = self.minimax(Marks.cross, boardCopy)
                    bestValue = min(val, bestValue)

            return bestValue
