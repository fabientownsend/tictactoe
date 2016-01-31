import unittest

from fake_console_io import FakeConsoleIO
from src.game_interface.game_interface import GameInterface

class TestGameInterface(unittest.TestCase):
    def setUp(self):
        self.fakeConsoleIO = FakeConsoleIO()
        self.gameInterface = GameInterface(self.fakeConsoleIO)
        self.fakeConsoleIO.spy_passed_into_method = False

    def test_display_type_game(self):
        self.gameInterface.display_type_game()
        self.assertTrue(self.fakeConsoleIO.spy_passed_into_method)

    def test_spot_not_free(self):
        self.gameInterface.spot_not_free()
        self.assertTrue(self.fakeConsoleIO.spy_passed_into_method)

    def test_display_correct_range_board(self):
        self.gameInterface.display_correct_range_board(0, 8)
        self.assertTrue(self.fakeConsoleIO.spy_passed_into_method)

    def test_get_type_game_selected(self):
        self.gameInterface.get_type_game_selected()

    def test_display_which_start(self):
        self.gameInterface.display_which_start()
        self.assertTrue(self.fakeConsoleIO.spy_passed_into_method)

    def test_get_first_player(self):
        first_player = self.gameInterface.get_first_player()
        self.assertEqual(first_player, 1)

    def test_display_player_turn(self):
        self.gameInterface.display_player_turn(None)
        self.assertTrue(self.fakeConsoleIO.spy_passed_into_method)

    def test_get_player_move(self):
        player_move = self.gameInterface.get_player_move()
        self.assertEqual(player_move, 1)

    def test_display_board(self):
        self.gameInterface.display_board(None)
        self.assertTrue(self.fakeConsoleIO.spy_passed_into_method)

    def test_display_winner(self):
        self.gameInterface.display_winner(None)
        self.assertTrue(self.fakeConsoleIO.spy_passed_into_method)

    def test_display_tie(self):
        self.gameInterface.display_tie()
        self.assertTrue(self.fakeConsoleIO.spy_passed_into_method)

    def test_expected_number(self):
        self.gameInterface.expected_number()
        self.assertTrue(self.fakeConsoleIO.spy_passed_into_method)
