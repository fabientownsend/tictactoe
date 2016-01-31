import unittest

from src.game_play.computer import Computer
from src.game_play.game_board import GameBoard
from src.game_play.marks_enum import Marks


class ComputerTest(unittest.TestCase):
    def setUp(self):
        self.computer = Computer(Marks.cross)

    def test_set_mark_when_cross(self):
        self.computer = Computer(Marks.cross)

        self.assertEqual(self.computer.mark, Marks.cross)

    def test_set_mark_when_nought(self):
        self.computer = Computer(Marks.nought)

        self.assertEqual(self.computer.mark, Marks.nought)

    def test_switch_when_mark_was_cross(self):
        noughtMark = self.computer.switch(Marks.cross)

        self.assertEqual(noughtMark, Marks.nought)

    def test_switch_when_mark_was_nought(self):
        crossMark = self.computer.switch(Marks.nought)

        self.assertEqual(crossMark, Marks.cross)

    def test_minimax_when_maximizing_player_win_score_positive(self):
        maximizing_player = Marks.cross
        self.game_board = GameBoard(3)
        self.game_board.set_mark(0, Marks.cross)
        self.game_board.set_mark(1, Marks.cross)
        self.game_board.set_mark(2, Marks.cross)

        positive_score = self.computer.minimax(maximizing_player,
                                               self.game_board)
        self.assertEqual(positive_score, 1)

    def test_minimax_when_minimizing_player_win_score_negative(self):
        maximizing_player = Marks.cross
        self.game_board = GameBoard(3)
        self.game_board.set_mark(0, Marks.nought)
        self.game_board.set_mark(1, Marks.nought)
        self.game_board.set_mark(2, Marks.nought)

        negative_score = self.computer.minimax(maximizing_player,
                                               self.game_board)
        self.assertEqual(negative_score, -1)

    def test_minimax_when_its_a_tie_score_neutral(self):
        maximizing_player = Marks.cross
        self.game_board = GameBoard(3)
        self.game_board.set_mark(0, Marks.nought)
        self.game_board.set_mark(1, Marks.cross)
        self.game_board.set_mark(2, Marks.nought)
        self.game_board.set_mark(3, Marks.nought)
        self.game_board.set_mark(4, Marks.cross)
        self.game_board.set_mark(5, Marks.cross)
        self.game_board.set_mark(6, Marks.cross)
        self.game_board.set_mark(7, Marks.nought)
        self.game_board.set_mark(8, Marks.cross)

        neutral_score = self.computer.minimax(maximizing_player,
                                              self.game_board)
        self.assertEqual(neutral_score, 0)

    def test_minimax_when_maximizing_player_win_in_both_different_move(self):
        maximizing_player = Marks.nought
        self.game_board = GameBoard(3)
        self.game_board.set_mark(0, Marks.empty)
        self.game_board.set_mark(1, Marks.cross)
        self.game_board.set_mark(2, Marks.nought)
        self.game_board.set_mark(3, Marks.empty)
        self.game_board.set_mark(4, Marks.cross)
        self.game_board.set_mark(5, Marks.cross)
        self.game_board.set_mark(6, Marks.nought)
        self.game_board.set_mark(7, Marks.nought)
        self.game_board.set_mark(8, Marks.cross)

        opportunity_move = self.computer.minimax(maximizing_player,
                                                  self.game_board)
        self.assertEqual(opportunity_move, 1)

    def test_minimax_when_opposant_win_in_both_different_move(self):
        maximizing_player = Marks.cross
        self.game_board = GameBoard(3)
        self.game_board.set_mark(0, Marks.empty)
        self.game_board.set_mark(1, Marks.nought)
        self.game_board.set_mark(2, Marks.cross)
        self.game_board.set_mark(3, Marks.empty)
        self.game_board.set_mark(4, Marks.nought)
        self.game_board.set_mark(5, Marks.nought)
        self.game_board.set_mark(6, Marks.cross)
        self.game_board.set_mark(7, Marks.cross)
        self.game_board.set_mark(8, Marks.nought)

        cant_win_with_this_move = self.computer.minimax(maximizing_player,
                                                        self.game_board)
        self.assertEqual(cant_win_with_this_move, -1)

    def test_get_move_when_maximizing_can_win(self):
        maximizing_player = Marks.cross
        self.game_board = GameBoard(3)
        self.game_board.set_mark(0, Marks.cross)
        self.game_board.set_mark(1, Marks.cross)

        win_move = self.computer.get_move(self.game_board)

        self.assertEqual(win_move, 2)

    def test_get_move_when_maximizing_should_block_opposant(self):
        maximizing_player = Marks.cross
        self.game_board = GameBoard(3)
        self.game_board.set_mark(0, Marks.nought)
        self.game_board.set_mark(1, Marks.nought)

        blocking_move = self.computer.get_move(self.game_board)

        self.assertEqual(blocking_move, 2)

    def test_get_move_when_maximizing_playe_create_opportunity_to_win(self):
        maximizing_player = Marks.cross
        self.game_board = GameBoard(3)
        self.game_board.set_mark(0, Marks.cross)
        self.game_board.set_mark(1, Marks.nought)
        self.game_board.set_mark(2, Marks.empty)
        self.game_board.set_mark(3, Marks.cross)
        self.game_board.set_mark(4, Marks.empty)
        self.game_board.set_mark(5, Marks.empty)
        self.game_board.set_mark(6, Marks.nought)
        self.game_board.set_mark(7, Marks.empty)
        self.game_board.set_mark(8, Marks.empty)

        opportunity_move = self.computer.get_move(self.game_board)

        self.assertEqual(opportunity_move, 4)

if __name__ == '__main__':
    unittest.main()
