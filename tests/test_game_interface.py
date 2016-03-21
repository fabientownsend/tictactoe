import unittest

from fake_console_io import FakeConsoleIO
from src.game_interface.english_messenger import EnglishMessenger


class TestGameInterface(unittest.TestCase):
    def setUp(self):
        self.fake_console_IO = FakeConsoleIO()
        self.game_interface = EnglishMessenger(self.fake_console_IO)
        self.fake_console_IO.spy_passed_into_method = False

    def test_display_type_game(self):
        type_game_message = ("Type of game:\n\n"
                     "1 - Human v. Human\n"
                     "2 - Human v. Computer\n"
                     "3 - Computer v. Computer\n"
                    )
        self.game_interface.display_type_game()
        self.assertTrue(self.fake_console_IO.spy_passed_into_method)
        self.assertEqual(self.fake_console_IO.displayed_value,
                         type_game_message)

    def test_spot_not_free(self):
        self.game_interface.spot_not_free()
        spot_not_free_message = "it must be a free spot"
        self.assertTrue(self.fake_console_IO.spy_passed_into_method)
        self.assertEqual(self.fake_console_IO.displayed_value,
                         spot_not_free_message)

    def test_display_correct_range_board(self):
        self.game_interface.display_range_board(0, 9)
        correct_range_message = "position between 0 and 8"
        self.assertTrue(self.fake_console_IO.spy_passed_into_method)
        self.assertEqual(self.fake_console_IO.displayed_value,
                         correct_range_message)

    def test_get_type_game_selected(self):
        game_selected = self.game_interface.get_type_game_selected()
        self.assertEqual(game_selected, 1)

    def test_display_which_start(self):
        player_start_message = ("Which player start:\n\n"
                             "1 - Player 1\n"
                             "2 - Player 2\n"
                            )
        self.game_interface.display_which_start()
        self.assertTrue(self.fake_console_IO.spy_passed_into_method)
        self.assertEqual(self.fake_console_IO.displayed_value,
                         player_start_message)

    def test_get_first_player(self):
        first_player = self.game_interface.get_first_player()
        self.assertEqual(first_player, 1)

    def test_display_player_turn(self):
        player_mark = 1
        player_turn_message = "Player " + str(player_mark) + " turn"
        self.game_interface.display_player_turn(player_mark)
        self.assertTrue(self.fake_console_IO.spy_passed_into_method)
        self.assertEqual(self.fake_console_IO.displayed_value,
                         player_turn_message)

    def test_get_player_move(self):
        player_move = self.game_interface.get_player_move()
        self.assertEqual(player_move, 1)

    def test_display_board(self):
        self.game_interface.display_board(None)
        self.assertTrue(self.fake_console_IO.spy_passed_into_method)

    def test_display_winner(self):
        winner_mark = 1
        winner_message = "Player " + str(winner_mark) + " won the party"
        self.game_interface.display_winner(winner_mark)
        self.assertTrue(self.fake_console_IO.spy_passed_into_method)
        self.assertEqual(self.fake_console_IO.displayed_value, winner_message)

    def test_display_tie(self):
        tie_message = "It's a tie, no one won!"
        self.game_interface.display_tie()
        self.assertTrue(self.fake_console_IO.spy_passed_into_method)
        self.assertEqual(self.fake_console_IO.displayed_value, tie_message)
