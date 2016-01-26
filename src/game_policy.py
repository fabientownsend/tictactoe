from marks_enum import Marks


class GamePolicy():
    def __init__(self):
        self.FIRST_DIAGONAL = 0
        self.SECOND_DIAGONAL = 1

    def check_tie(self, board):
        if (self.is_full(board) and not
            self.win(board, Marks.nought) and not
            self.win(board, Marks.cross)):
            return True
        else:
            return False

    def is_full(self, board):
        for row in board:
            for cell in row:
                if cell == Marks.empty:
                    return False

        return True

    def win(self, board, mark):
        for num in range(len(board)):
            if self.row_win(num, board, mark):
                return True
            if self.column_win(num, board, mark):
                return True

        if self.diagonal_win(self.FIRST_DIAGONAL, board, mark):
            return True
        if self.diagonal_win(self.SECOND_DIAGONAL, board, mark):
            return True

        return False

    def row_win(self, num, board, mark):
        for row in board[num]:
            if not row == mark:
                return False

        return True

    def column_win(self, num, board, mark):
        for row in range(len(board[num])):
            if not board[row][num] == mark:
                return False

        return True

    def diagonal_win(self, num, board, mark):
        if num == self.FIRST_DIAGONAL:
            for position in range(len(board)):
                if not board[position][position] == mark:
                    return False

        if num == self.SECOND_DIAGONAL:
            for position in range(len(board)):
                if not board[position][len(board) - position - 1] == mark:
                    return False

        return True
