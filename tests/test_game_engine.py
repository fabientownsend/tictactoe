import unittest

from computer import Computer
from fake_console_ui import FakeConsoleUI
from fake_game_policy import FakeGamePolicy
from fake_player import FakePlayer
from game_board import GameBoard
from game_engine import GameEngine
from game_engine import PlayersEnum
from human import Human
from marks_enum import Marks


class GameEngineTest(unittest.TestCase):
    def setUp(self):
        self.fake_console = FakeConsoleUI()
        self.fake_game_policy = FakeGamePolicy()
        self.fake_board = GameBoard(3)
        self.game_engine = GameEngine(
            self.fake_console,
            self.fake_game_policy,
            self.fake_board)
        self.game_engine.create_type_game()

    def testCreatePlayer_whenTwoHuman(self):
        self.game_engine.create_players_type_game(1)
        self.assertTrue(isinstance(self.game_engine.player_1, Human))
        self.assertTrue(isinstance(self.game_engine.player_2, Human))

    def testCreatePlayer_whenHumanAndComputer(self):
        self.game_engine.create_players_type_game(2)
        self.assertTrue(isinstance(self.game_engine.player_1, Human))
        self.assertTrue(isinstance(self.game_engine.player_2, Computer))

    def testCreatePlayer_whenTwoComputer(self):
        self.game_engine.create_players_type_game(3)
        self.assertTrue(isinstance(self.game_engine.player_1, Computer))
        self.assertTrue(isinstance(self.game_engine.player_2, Computer))

    def testSetFirstPlayer_whenFirstPlayerIsPlayer1(self):
        self.game_engine.create_players_type_game(1)
        self.game_engine.set_first_player(1)
        self.assertEqual(self.game_engine.current_player, self.game_engine.player_1)

    def testSetFirstPlayer_whenFirstPlayerIsPlayer2(self):
        self.game_engine.create_players_type_game(2)
        self.game_engine.set_first_player(2)
        self.assertEqual(self.game_engine.current_player, self.game_engine.player_2)

    def testSwitchPlayer_whenCurrentPlayerWasPlayer1(self):
        self.game_engine.create_players_type_game(2)
        self.game_engine.current_player = self.game_engine.player_1
        self.game_engine.switch_current_player()
        self.assertEqual(self.game_engine.current_player, self.game_engine.player_2)

    def testSwitchPlayer_whenCurrentPlayerWasPlayer2(self):
        self.game_engine.create_players_type_game(2)
        self.game_engine.current_player = self.game_engine.player_2
        self.game_engine.switch_current_player()
        self.assertEqual(self.game_engine.current_player, self.game_engine.player_1)

    def testWin_whenItsNotWin(self):
        self.assertFalse(self.game_engine.game_over)

    def testGetTypeGameSelected_whenSelect2(self):
        typePartySelected = self.game_engine.get_type_game_selected()
        self.assertEqual(typePartySelected, 2)

    def testGetFirstPlayersSelected_whenFirstPlayerPlayer1(self):
        first_player_selected = self.game_engine.get_first_player_selected()
        self.assertEqual(first_player_selected, 1)

    def testIsGameOver_whenAPlayerWin(self):
        fake_board = None
        self.game_engine.create_players_type_game(2)
        self.game_engine.set_first_player(2)
        self.fake_game_policy.response_win = True
        self.fake_game_policy.response_check_tie = False

        self.assertTrue(self.game_engine.is_game_over(fake_board))
        self.assertTrue(self.game_engine.game_over)
        self.assertFalse(self.game_engine.tie)

    def testIsGameOver_whenItsATie(self):
        fake_board = None
        self.game_engine.create_players_type_game(2)
        self.game_engine.set_first_player(2)
        self.fake_game_policy.response_win = False
        self.fake_game_policy.response_check_tie = True

        self.assertTrue(self.game_engine.is_game_over(fake_board))
        self.assertTrue(self.game_engine.tie)
        self.assertTrue(self.game_engine.game_over)

    def testIsGameOver_whenItsNotGameOverNeitherTie(self):
        fake_board = None
        self.game_engine.create_players_type_game(2)
        self.game_engine.set_first_player(2)
        self.fake_game_policy.response_win = False
        self.fake_game_policy.response_check_tie = False

        self.assertFalse(self.game_engine.is_game_over(fake_board))
        self.assertFalse(self.game_engine.tie)
        self.assertFalse(self.game_engine.game_over)

    def testCreateTypeGame_whenCreateGameHumanVsComputer(self):
        self.assertTrue(isinstance(self.game_engine.player_1, Human))
        self.assertTrue(isinstance(self.game_engine.player_2, Computer))

    def testDefineFirstPlayer(self):
        self.game_engine.define_first_player()
        self.assertEqual(self.game_engine.current_player, self.game_engine.player_1)

    def testDisplayResult_whenItsATie(self):
        self.game_engine.tie = True
        self.game_engine.display_result()
        self.assertTrue(self.fake_console.passed_in_display_tie)

    def testDisplayResult_whenAPlayerWin(self):
        self.game_engine.tie = False
        self.game_engine.winner = self.game_engine.player_1
        self.game_engine.display_result()
        self.assertTrue(self.fake_console.passed_in_display_winner)

    def testPlay_whenPlayerCrossWinTheParty(self):
        fakePlayer = FakePlayer(Marks.cross)
        self.game_engine.current_player = fakePlayer
        self.fake_board.board[0][0] = Marks.empty
        self.fake_board.board[0][1] = Marks.cross
        self.fake_board.board[0][2] = Marks.cross
        self.fake_board.board[1][0] = Marks.nought
        self.fake_board.board[1][1] = Marks.nought
        self.fake_board.board[1][2] = Marks.cross
        self.fake_board.board[2][0] = Marks.nought
        self.fake_board.board[2][1] = Marks.cross
        self.fake_board.board[2][2] = Marks.nought
        self.fake_game_policy.response_win = True

        self.game_engine.play()

        self.assertFalse(self.game_engine.tie)
        self.assertTrue(self.game_engine.game_over)
        self.assertEqual(self.game_engine.winner, fakePlayer)

    def testPlay_whenPlayerNoughtWinTheParty(self):
        fakePlayer = FakePlayer(Marks.nought)
        self.game_engine.current_player = fakePlayer
        self.fake_board.board[0][0] = Marks.empty
        self.fake_board.board[0][1] = Marks.cross
        self.fake_board.board[0][2] = Marks.cross
        self.fake_board.board[1][0] = Marks.nought
        self.fake_board.board[1][1] = Marks.nought
        self.fake_board.board[1][2] = Marks.cross
        self.fake_board.board[2][0] = Marks.nought
        self.fake_board.board[2][1] = Marks.cross
        self.fake_board.board[2][2] = Marks.nought
        self.fake_game_policy.response_win = True

        self.game_engine.play()

        self.assertFalse(self.game_engine.tie)
        self.assertTrue(self.game_engine.game_over)
        self.assertEqual(self.game_engine.winner, fakePlayer)

    def testPlay_whenPartyIsATie(self):
        fakePlayer = FakePlayer(Marks.cross)
        self.game_engine.current_player = fakePlayer
        self.fake_board.board[0][0] = Marks.cross
        self.fake_board.board[0][1] = Marks.nought
        self.fake_board.board[0][2] = Marks.cross
        self.fake_board.board[1][0] = Marks.nought
        self.fake_board.board[1][1] = Marks.nought
        self.fake_board.board[1][2] = Marks.cross
        self.fake_board.board[2][0] = Marks.nought
        self.fake_board.board[2][1] = Marks.cross
        self.fake_board.board[2][2] = Marks.nought
        self.fake_game_policy.response_win = False
        self.fake_game_policy.response_check_tie = True

        self.game_engine.play()

        self.assertTrue(self.game_engine.tie)
        self.assertTrue(self.game_engine.game_over)
        self.assertEqual(self.game_engine.winner, None)

    def testPlay_whenPlayerSwitch(self):
        self.fake_game_policy.response_win = False
        self.fake_game_policy.response_check_tie = False
        fakePlayerOne = FakePlayer(Marks.cross)
        fakePlayerTwo = FakePlayer(Marks.nought)
        self.game_engine.player_1 = fakePlayerOne
        self.game_engine.player_2 = fakePlayerTwo
        self.game_engine.current_player = fakePlayerOne

        self.game_engine.play()

        self.assertEqual(self.game_engine.current_player, fakePlayerTwo)

if __name__ == '__main__':
    unittest.main()
