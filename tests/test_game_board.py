import unittest

from src.game_play.game_board import GameBoard
from src.game_play.marks_enum import Marks


class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.board_width = 3
        self.game_board = GameBoard(self.board_width)
        self.new_game_board = self.game_board.create_board()

    def get_empty_board(self, board_width):
        return [[Marks.empty]*board_width for n in range(board_width)]

    def test_create_baord_when_board_width_three(self):
        empty_game_board = self.get_empty_board(self.board_width)

        self.assertEqual(self.new_game_board, empty_game_board)

    def test_get_max_range_when_board_width_three(self):
        board_width = 3
        range_max = board_width*board_width
        game_board = GameBoard(board_width)

        self.assertEqual(game_board.get_max_range(), range_max)

    def test_get_min_range(self):
        range_min = 0
        self.assertEqual(self.game_board.get_min_range(), range_min)

    def test_create_baord_when_board_width_four(self):
        board_width = 4
        empty_game_board = self.get_empty_board(board_width)
        game_board = GameBoard(board_width)

        self.assertEqual(game_board.board, empty_game_board)

    def test_set_mark_when_spot_empty(self):
        position = 0
        self.game_board.set_mark(position, Marks.cross)
        mark_set_on_board = self.game_board.get_mark(position)

        self.assertEqual(Marks.cross, mark_set_on_board)

    def test_is_empty_when_spot_is_empty(self):
        position = 0
        self.game_board.set_mark(position, Marks.cross)

        self.assertFalse(self.game_board.is_empty(position))

    def test_set_mark_when_out_of_the_board(self):
        position = 10

        with self.assertRaises(IndexError):
            self.game_board.set_mark(position, Marks.cross)

if __name__ == '__main__':
    unittest.main()
