import unittest

from fake_game_interface import FakeGameInterface

from src.game_play.computer import Computer
from src.game_play.human import Human
from src.game_play.players_application import PlayersApplicationImp


class TestPlayersApplication(unittest.TestCase):
    def setUp(self):
        fake_game_interface = FakeGameInterface()
        self.players_application = PlayersApplicationImp(fake_game_interface)
        self.human_vs_human = 1
        self.human_vs_computer = 2
        self.computer_vs_computer = 3
        self.player_1 = 1
        self.player_2 = 2

    def test_create_player_when_two_human(self):
        self.players_application.create_players_type_game(self.human_vs_human)

        self.assertTrue(isinstance(self.players_application.player_1, Human))
        self.assertTrue(isinstance(self.players_application.player_2, Human))

    def test_create_player_when_human_vs_computer(self):
        self.players_application.create_players_type_game(self.human_vs_computer)

        self.assertTrue(isinstance(self.players_application.player_1, Human))
        self.assertTrue(isinstance(self.players_application.player_2, Computer))

    def test_create_player_when_computer_vs_computer(self):
        self.players_application.create_players_type_game(self.computer_vs_computer)
        self.assertTrue(isinstance(self.players_application.player_1, Computer))

        self.assertTrue(isinstance(self.players_application.player_2, Computer))

    def test_test_first_player_when_first_player_is_player_one(self):
        self.players_application.create_players_type_game(self.human_vs_human)
        self.players_application.set_first_player(self.player_1)

        self.assertEqual(self.players_application.current_player,
                         self.players_application.player_1)

    def test_test_first_player_when_first_player_is_player_two(self):
        self.players_application.create_players_type_game(self.human_vs_computer)
        self.players_application.set_first_player(self.player_2)

        self.assertEqual(self.players_application.current_player,
                         self.players_application.player_2)

    def test_switch_player_when_current_player_was_player_one(self):
        self.players_application.create_players_type_game(self.human_vs_computer)
        self.players_application.current_player = self.players_application.player_1
        self.players_application.switch_current_player()

        self.assertEqual(self.players_application.current_player,
                         self.players_application.player_2)

    def test_switch_player_when_current_player_was_player_two(self):
        self.players_application.create_players_type_game(self.human_vs_computer)
        self.players_application.current_player = self.players_application.player_2
        self.players_application.switch_current_player()

        self.assertEqual(self.players_application.current_player,
                         self.players_application.player_1)
