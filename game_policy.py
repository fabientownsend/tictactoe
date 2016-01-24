from marks_enum import Marks


class GamePolicy():
    def checkTie(self, board):
        if (
            self.isFull(board) and not
            self.win(board, Marks.nought) and not
            self.win(board, Marks.cross)
            ):
            return True
        else:
            return False

    def isFull(self, board):
        for row in board:
            for cell in row:
                if cell == Marks.empty:
                    return False

        return True

    def win(self, board, mark):
        for num in range(len(board)):
            if self.rowMarked(num, board, mark):
                return True
            if self.columnMarked(num, board, mark):
                return True
        if self.diagonalMarked(0, board, mark):
            return True
        if self.diagonalMarked(1, board, mark):
            return True
        return False

    def rowMarked(self, num, board, mark):
        for row in board[num]:
            if not row == mark:
                return False
        return True

    def columnMarked(self, num, board, mark):
        for row in range(len(board[num])):
            if not board[row][num] == mark:
                return False
        return True

    def diagonalMarked(self, num, board, mark):
        if num == 0:
            for position in range(len(board)):
                if not board[position][position] == mark:
                    return False
        if num == 1:
            for position in range(len(board)):
                if not board[position][len(board) - position - 1] == mark:
                    return False

        return True
