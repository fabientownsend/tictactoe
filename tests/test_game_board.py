import unittest

from game_board import GameBoard
from marks_enum import Marks


class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.board_size = 3
        self.game_board = GameBoard(self.board_size)
        self.new_game_board = self.game_board.create_board()

    def get_empty_board(self, board_size):
        return [[Marks.empty]*board_size for n in range(board_size)]

    def test_create_baord_when_board_size_three(self):
        empty_game_board = self.get_empty_board(self.board_size)
        self.assertEqual(self.new_game_board, empty_game_board)

    def test_create_baord_when_board_size_four(self):
        board_size = 4
        empty_game_board = self.get_empty_board(board_size)
        game_board = GameBoard(board_size)
        new_game_board = game_board.create_board()
        self.assertEqual(new_game_board, empty_game_board)

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
