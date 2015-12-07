from marksEnum import Marks
from copy import copy

class Minimax():
    def checkTie(self, board):
        for i in board:
            if i == Marks.empty:
                return False
        return True

    def bestMove(self, mark, board):
        bestMove = 0
        for i in board:
            self.boardCopy = copy(board)
            self.setMark(i, Marks.cross)
            if self.win(mark, self.boardCopy):
                bestMove = i

        return bestMove

    def setMark(self, position, mark):
        print self.boardCopy[position]
        if self.boardCopy[position] != Marks.empty:
            raise SpotNotEmpty
        else:
            self.boardCopy[position] = mark

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

    def minimax(self, mark, board):
        print board
        if mark == Marks.cross and self.win(mark, board):
            return 1
        elif mark == Marks.nought and self.win(mark, board):
            return -1
        elif self.checkTie(board):
            return 0
