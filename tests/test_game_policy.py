import unittest

from src.game_play.game_policy import GamePolicy
from src.game_play.marks_enum import Marks


class GamePolicyTest(unittest.TestCase):
    def setUp(self):
        self.game_policy = GamePolicy()
        self.board_width = 3

    def get_empty_board(self, board_width):
        return [[Marks.empty]*board_width for n in range(board_width)]

    def test_is_full_when_its_empty(self):
        empty_board = self.get_empty_board(self.board_width)

        self.assertFalse(self.game_policy.is_full(empty_board))

    def test_is_full_when_its_not_empty(self):
        board = self.get_empty_board(self.board_width)
        board[0][0] = Marks.cross

        self.assertFalse(self.game_policy.is_full(board))

    def test_win_when_rows_are_win(self):
        mark = Marks.cross
        board = self.get_empty_board(self.board_width)

        for row in range(len(board)):
            board = self.set_mark_row(board, mark, row)

            self.assertTrue(self.game_policy.row_win(row, board, mark))
            self.assertTrue(self.game_policy.win(board, Marks.cross))

    def set_mark_row(self, board, mark, row):
        for column in range(len(board)):
            board[row][column] = mark

        return board

    def test_win_when_column_are_win(self):
        mark = Marks.cross
        board = self.get_empty_board(self.board_width)

        for column in range(len(board)):
            board = self.set_mark_column(board, mark, column)

            self.assertTrue(self.game_policy.column_win(column, board, mark))
            self.assertTrue(self.game_policy.win(board, Marks.cross))

    def set_mark_column(self, board, mark, column):
        for row in range(len(board)):
            board[row][column] = mark

        return board

    def test_win_when_dial_one_win(self):
        diagonal = 0
        mark = Marks.cross
        board = self.get_empty_board(self.board_width)

        for position in range(self.board_width):
            board[position][position] = mark

        self.assertTrue(self.game_policy.diagonal_win(diagonal, board, mark))
        self.assertTrue(self.game_policy.win(board, mark))

    def test_win_when_dial_two_win(self):
        diagonal = 1
        mark = Marks.cross
        board = self.get_empty_board(self.board_width)

        for position in range(self.board_width):
            board[position][self.board_width - position - 1] = mark

        self.assertTrue(self.game_policy.diagonal_win(diagonal, board, mark))
        self.assertTrue(self.game_policy.win(board, mark))

    def test_check_tie_when_its_tie(self):
        board = self.get_empty_board(self.board_width)
        board[0][0] = Marks.cross
        board[0][1] = Marks.nought
        board[0][2] = Marks.cross
        board[1][0] = Marks.nought
        board[1][1] = Marks.nought
        board[1][2] = Marks.cross
        board[2][0] = Marks.nought
        board[2][1] = Marks.cross
        board[2][2] = Marks.nought

        self.assertTrue(self.game_policy.check_tie(board))

    def test_check_tie_when_board_is_not_full(self):
        board = self.get_empty_board(self.board_width)
        board[0][0] = Marks.cross
        board[0][1] = Marks.nought
        board[0][2] = Marks.cross
        board[1][0] = Marks.empty
        board[1][1] = Marks.nought
        board[1][2] = Marks.cross
        board[2][0] = Marks.nought
        board[2][1] = Marks.cross
        board[2][2] = Marks.nought

        self.assertFalse(self.game_policy.check_tie(board))

    def test_check_tie_when_its_full_and_win(self):
        board = self.get_empty_board(self.board_width)
        board[0][0] = Marks.cross
        board[0][1] = Marks.cross
        board[0][2] = Marks.cross
        board[1][0] = Marks.cross
        board[1][1] = Marks.cross
        board[1][2] = Marks.cross
        board[2][0] = Marks.cross
        board[2][1] = Marks.cross
        board[2][2] = Marks.cross

        self.assertFalse(self.game_policy.check_tie(board))

if __name__ == '__main__':
    unittest.main()
