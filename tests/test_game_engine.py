import unittest

from fake_game_interface import FakeGameInterface
from fake_game_policy import FakeGamePolicy
from fake_player import FakePlayer

from src.game_play.computer import Computer
from src.game_play.game_board import GameBoard
from src.game_play.game_engine import GameEngine
from src.game_play.game_engine import PlayersEnum
from src.game_play.human import Human
from src.game_play.marks_enum import Marks


class GameEngineTest(unittest.TestCase):
    def setUp(self):
        self.fake_game_interface = FakeGameInterface()
        self.fake_game_policy = FakeGamePolicy()
        self.fake_board = GameBoard(3)
        self.game_engine = GameEngine(self.fake_game_interface,
                                      self.fake_game_policy,
                                      self.fake_board)
        self.game_engine.create_type_game()

    def test_create_player_when_two_human(self):
        self.game_engine.create_players_type_game(1)

        self.assertTrue(isinstance(self.game_engine.player_1, Human))
        self.assertTrue(isinstance(self.game_engine.player_2, Human))

    def test_create_player_when_human_vs_computer(self):
        self.game_engine.create_players_type_game(2)

        self.assertTrue(isinstance(self.game_engine.player_1, Human))
        self.assertTrue(isinstance(self.game_engine.player_2, Computer))

    def test_create_player_when_computer_vs_computer(self):
        self.game_engine.create_players_type_game(3)
        self.assertTrue(isinstance(self.game_engine.player_1, Computer))

        self.assertTrue(isinstance(self.game_engine.player_2, Computer))

    def test_test_first_player_when_first_player_is_player_one(self):
        self.game_engine.create_players_type_game(1)
        self.game_engine.set_first_player(1)

        self.assertEqual(self.game_engine.current_player,
                         self.game_engine.player_1)

    def test_test_first_player_when_first_player_is_player_two(self):
        self.game_engine.create_players_type_game(2)
        self.game_engine.set_first_player(2)

        self.assertEqual(self.game_engine.current_player,
                         self.game_engine.player_2)

    def test_switch_player_when_current_player_was_player_one(self):
        self.game_engine.create_players_type_game(2)
        self.game_engine.current_player = self.game_engine.player_1
        self.game_engine.switch_current_player()

        self.assertEqual(self.game_engine.current_player,
                         self.game_engine.player_2)

    def test_switch_player_when_current_player_was_player_two(self):
        self.game_engine.create_players_type_game(2)
        self.game_engine.current_player = self.game_engine.player_2
        self.game_engine.switch_current_player()

        self.assertEqual(self.game_engine.current_player,
                         self.game_engine.player_1)

    def test_win_when_its_not_win(self):
        self.assertFalse(self.game_engine.game_over)

    def test_get_type_game_selected_when_select_two(self):
        self.fake_game_interface.gameSelected = 1
        typePartySelected = self.game_engine.get_type_game_selected()

        self.assertEqual(typePartySelected, 1)

    def test_get_first_player_selected_when_first_was_player_one(self):
        self.fake_game_interface.first_player = 1
        first_player_selected = self.game_engine.get_first_player_selected()

        self.assertEqual(first_player_selected, 1)

    def test_get_first_player_selected_when_pass_twice_in_the_method(self):
        self.fake_game_interface.first_player = 15
        self.fake_game_interface.get_first_player_counter = 0

        first_player_selected = self.game_engine.get_first_player_selected()

        self.assertEqual(self.fake_game_interface.get_first_player_counter, 2)
        self.assertEqual(first_player_selected, 1)

    def test_is_game_over_when_a_player_win(self):
        fake_board = None
        self.game_engine.create_players_type_game(2)
        self.game_engine.set_first_player(2)
        self.fake_game_policy.response_win = True
        self.fake_game_policy.response_check_tie = False

        self.assertTrue(self.game_engine.is_game_over(fake_board))

    def test_is_game_over_when_its_a_tie(self):
        fake_board = None
        self.game_engine.create_players_type_game(2)
        self.game_engine.set_first_player(2)
        self.fake_game_policy.response_win = False
        self.fake_game_policy.response_check_tie = True

        self.assertTrue(self.game_engine.is_game_over(fake_board))

    def test_is_game_over_when_its_not_game_over_either_tie(self):
        fake_board = None
        self.game_engine.create_players_type_game(2)
        self.game_engine.set_first_player(2)
        self.fake_game_policy.response_win = False
        self.fake_game_policy.response_check_tie = False

        self.assertFalse(self.game_engine.is_game_over(fake_board))

    def test_set_game_result_when_a_player_win(self):
        fake_board = None
        self.game_engine.create_players_type_game(2)
        self.game_engine.set_first_player(2)
        self.fake_game_policy.response_win = True
        self.fake_game_policy.response_check_tie = False

        self.game_engine.set_game_result(fake_board)

        self.assertTrue(self.game_engine.game_over)
        self.assertFalse(self.game_engine.tie)

    def test_set_game_result_when_its_a_tie(self):
        fake_board = None
        self.game_engine.create_players_type_game(2)
        self.game_engine.set_first_player(2)
        self.fake_game_policy.response_win = False
        self.fake_game_policy.response_check_tie = True

        self.game_engine.set_game_result(fake_board)

        self.assertTrue(self.game_engine.tie)
        self.assertTrue(self.game_engine.game_over)

    def test_create_type_game_when_create_game_human_vs_computer(self):
        self.game_engine.create_type_game()
        self.game_engine.create_players_type_game(2)

        self.assertTrue(isinstance(self.game_engine.player_1, Human))
        self.assertTrue(isinstance(self.game_engine.player_2, Computer))

    def test_define_first_player(self):
        self.game_engine.define_first_player()

        self.assertEqual(self.game_engine.current_player,
                         self.game_engine.player_1)

    def test_display_result_when_its_a_tie(self):
        self.game_engine.tie = True
        self.game_engine.display_result()

        self.assertTrue(self.fake_game_interface.passed_in_display_tie)

    def test_display_result_when_a_player_win(self):
        self.game_engine.tie = False
        self.game_engine.winner = self.game_engine.player_1
        self.game_engine.display_result()

        self.assertTrue(self.fake_game_interface.passed_in_display_winner)

    def test_play_when_player_cross_win(self):
        fake_player = FakePlayer(Marks.cross)
        self.game_engine.current_player = fake_player
        self.fake_game_policy.response_win = True

        self.game_engine.play()

        self.assertFalse(self.game_engine.tie)
        self.assertTrue(self.game_engine.game_over)
        self.assertEqual(self.game_engine.winner, fake_player)

    def test_play_when_player_nought_win(self):
        fake_player = FakePlayer(Marks.nought)
        self.game_engine.current_player = fake_player
        self.fake_game_policy.response_win = True

        self.game_engine.play()

        self.assertFalse(self.game_engine.tie)
        self.assertTrue(self.game_engine.game_over)
        self.assertEqual(self.game_engine.winner, fake_player)

    def test_play_when_party_is_a_tie(self):
        fake_player = FakePlayer(Marks.cross)
        self.game_engine.current_player = fake_player
        self.fake_game_policy.response_win = False
        self.fake_game_policy.response_check_tie = True

        self.game_engine.play()

        self.assertTrue(self.game_engine.tie)
        self.assertTrue(self.game_engine.game_over)
        self.assertEqual(self.game_engine.winner, None)

    def test_play_when_player_switch(self):
        self.fake_game_policy.response_win = False
        self.fake_game_policy.response_check_tie = False
        fake_player_one = FakePlayer(Marks.cross)
        fake_player_two = FakePlayer(Marks.nought)
        self.game_engine.player_1 = fake_player_one
        self.game_engine.player_2 = fake_player_two
        self.game_engine.current_player = fake_player_one

        self.game_engine.play()

        self.assertEqual(self.game_engine.current_player, fake_player_two)

if __name__ == '__main__':
    unittest.main()
