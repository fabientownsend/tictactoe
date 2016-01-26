import unittest

from fake_console_ui import FakeConsoleUI

from src.game_board import GameBoard
from src.human import Human
from src.marks_enum import Marks


class TestHuman(unittest.TestCase):
    def setUp(self):
        self.fake_console_ui = FakeConsoleUI()

    def test_set_mark_when_mark_is_cross(self):
        self.human = Human(Marks.cross, self.fake_console_ui)
        self.assertEqual(self.human.mark, Marks.cross)

    def test_set_mark_when_mark_is_nought(self):
        self.human = Human(Marks.nought, self.fake_console_ui)
        self.assertEqual(self.human.mark, Marks.nought)

    def test_get_move_when_value_valide(self):
        self.fake_console_ui.player_move_position = 5
        self.human = Human(Marks.nought, self.fake_console_ui)
        self.game_board = GameBoard(3)

        self.assertEqual(self.human.get_move(self.game_board), 5)

    def test_get_move_when_get_value_too_low(self):
        self.fake_console_ui.player_move_position = -10
        self.human = Human(Marks.nought, self.fake_console_ui)
        self.game_board = GameBoard(3)

        self.human.get_move(self.game_board)

        self.assertTrue(self.fake_console_ui.passed_in_wrong_range)

    def test_get_move_when_its_a_free_spot(self):
        self.fake_console_ui.player_move_position = 1
        self.human = Human(Marks.nought, self.fake_console_ui)
        self.game_board = GameBoard(3)
        self.game_board.set_mark(1, Marks.cross)

        self.human.get_move(self.game_board)

        self.assertTrue(self.fake_console_ui.passed_in_spot_not_free)

if __name__ == '__main__':
    unittest.main()
