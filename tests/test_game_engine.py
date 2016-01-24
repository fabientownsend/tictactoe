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
        self.fakeConsole = FakeConsoleUI()
        self.fakeGamePolicy = FakeGamePolicy()
        self.fakeBoard = GameBoard(3)
        self.gameEngine = GameEngine(
            self.fakeConsole,
            self.fakeGamePolicy,
            self.fakeBoard)
        self.gameEngine.createTypeGame()

    def testCreatePlayer_whenTwoHuman(self):
        self.gameEngine.createPlayersTypeGame(1)
        self.assertTrue(isinstance(self.gameEngine.player1, Human))
        self.assertTrue(isinstance(self.gameEngine.player2, Human))

    def testCreatePlayer_whenHumanAndComputer(self):
        self.gameEngine.createPlayersTypeGame(2)
        self.assertTrue(isinstance(self.gameEngine.player1, Human))
        self.assertTrue(isinstance(self.gameEngine.player2, Computer))

    def testCreatePlayer_whenTwoComputer(self):
        self.gameEngine.createPlayersTypeGame(3)
        self.assertTrue(isinstance(self.gameEngine.player1, Computer))
        self.assertTrue(isinstance(self.gameEngine.player2, Computer))

    def testSetFirstPlayer_whenFirstPlayerIsPlayer1(self):
        self.gameEngine.createPlayersTypeGame(1)
        self.gameEngine.setFirstPlayer(1)
        self.assertEqual(self.gameEngine.currentPlayer, self.gameEngine.player1)

    def testSetFirstPlayer_whenFirstPlayerIsPlayer2(self):
        self.gameEngine.createPlayersTypeGame(2)
        self.gameEngine.setFirstPlayer(2)
        self.assertEqual(self.gameEngine.currentPlayer, self.gameEngine.player2)

    def testSwitchPlayer_whenCurrentPlayerWasPlayer1(self):
        self.gameEngine.createPlayersTypeGame(2)
        self.gameEngine.currentPlayer = self.gameEngine.player1
        self.gameEngine.switchCurrentPlayer()
        self.assertEqual(self.gameEngine.currentPlayer, self.gameEngine.player2)

    def testSwitchPlayer_whenCurrentPlayerWasPlayer2(self):
        self.gameEngine.createPlayersTypeGame(2)
        self.gameEngine.currentPlayer = self.gameEngine.player2
        self.gameEngine.switchCurrentPlayer()
        self.assertEqual(self.gameEngine.currentPlayer, self.gameEngine.player1)

    def testWin_whenItsNotWin(self):
        self.assertFalse(self.gameEngine.gameOver)

    def testGetTypeGameSelected_whenSelect2(self):
        typePartySelected = self.gameEngine.getTypeGameSelected()
        self.assertEqual(typePartySelected, 2)

    def testGetFirstPlayersSelected_whenFirstPlayerPlayer1(self):
        firstPlayerSelected = self.gameEngine.getFirstPlayerSlected()
        self.assertEqual(firstPlayerSelected, 1)

    def testIsGameOver_whenAPlayerWin(self):
        fakeBoard = None
        self.gameEngine.createPlayersTypeGame(2)
        self.gameEngine.setFirstPlayer(2)
        self.fakeGamePolicy.responseWin = True
        self.fakeGamePolicy.responseCheckTie = False

        self.assertTrue(self.gameEngine.isGameOver(fakeBoard))
        self.assertTrue(self.gameEngine.gameOver)
        self.assertFalse(self.gameEngine.tie)

    def testIsGameOver_whenItsATie(self):
        fakeBoard = None
        self.gameEngine.createPlayersTypeGame(2)
        self.gameEngine.setFirstPlayer(2)
        self.fakeGamePolicy.responseWin = False
        self.fakeGamePolicy.responseCheckTie = True

        self.assertTrue(self.gameEngine.isGameOver(fakeBoard))
        self.assertTrue(self.gameEngine.tie)
        self.assertTrue(self.gameEngine.gameOver)

    def testIsGameOver_whenItsNotGameOverNeitherTie(self):
        fakeBoard = None
        self.gameEngine.createPlayersTypeGame(2)
        self.gameEngine.setFirstPlayer(2)
        self.fakeGamePolicy.responseWin = False
        self.fakeGamePolicy.responseCheckTie = False

        self.assertFalse(self.gameEngine.isGameOver(fakeBoard))
        self.assertFalse(self.gameEngine.tie)
        self.assertFalse(self.gameEngine.gameOver)

    def testCreateTypeGame_whenCreateGameHumanVsComputer(self):
        self.assertTrue(isinstance(self.gameEngine.player1, Human))
        self.assertTrue(isinstance(self.gameEngine.player2, Computer))

    def testDefineFirstPlayer(self):
        self.gameEngine.defineFirstPlayer()
        self.assertEqual(self.gameEngine.currentPlayer, self.gameEngine.player1)

    def testDisplayResult_whenItsATie(self):
        self.gameEngine.tie = True
        self.gameEngine.displayResult()
        self.assertTrue(self.fakeConsole.passedIntoDisplayTie)

    def testDisplayResult_whenAPlayerWin(self):
        self.gameEngine.tie = False
        self.gameEngine.winner = self.gameEngine.player1
        self.gameEngine.displayResult()
        self.assertTrue(self.fakeConsole.passedIntoDisplayWinner)

    def testPlay_whenPlayerCrossWinTheParty(self):
        fakePlayer = FakePlayer(Marks.cross)
        self.gameEngine.currentPlayer = fakePlayer
        self.fakeBoard.board[0][0] = Marks.empty
        self.fakeBoard.board[0][1] = Marks.cross
        self.fakeBoard.board[0][2] = Marks.cross
        self.fakeBoard.board[1][0] = Marks.nought
        self.fakeBoard.board[1][1] = Marks.nought
        self.fakeBoard.board[1][2] = Marks.cross
        self.fakeBoard.board[2][0] = Marks.nought
        self.fakeBoard.board[2][1] = Marks.cross
        self.fakeBoard.board[2][2] = Marks.nought
        self.fakeGamePolicy.responseWin = True

        self.gameEngine.play()

        self.assertFalse(self.gameEngine.tie)
        self.assertTrue(self.gameEngine.gameOver)
        self.assertEqual(self.gameEngine.winner, fakePlayer)

    def testPlay_whenPlayerNoughtWinTheParty(self):
        fakePlayer = FakePlayer(Marks.nought)
        self.gameEngine.currentPlayer = fakePlayer
        self.fakeBoard.board[0][0] = Marks.empty
        self.fakeBoard.board[0][1] = Marks.cross
        self.fakeBoard.board[0][2] = Marks.cross
        self.fakeBoard.board[1][0] = Marks.nought
        self.fakeBoard.board[1][1] = Marks.nought
        self.fakeBoard.board[1][2] = Marks.cross
        self.fakeBoard.board[2][0] = Marks.nought
        self.fakeBoard.board[2][1] = Marks.cross
        self.fakeBoard.board[2][2] = Marks.nought
        self.fakeGamePolicy.responseWin = True

        self.gameEngine.play()

        self.assertFalse(self.gameEngine.tie)
        self.assertTrue(self.gameEngine.gameOver)
        self.assertEqual(self.gameEngine.winner, fakePlayer)

    def testPlay_whenPartyIsATie(self):
        fakePlayer = FakePlayer(Marks.cross)
        self.gameEngine.currentPlayer = fakePlayer
        self.fakeBoard.board[0][0] = Marks.cross
        self.fakeBoard.board[0][1] = Marks.nought
        self.fakeBoard.board[0][2] = Marks.cross
        self.fakeBoard.board[1][0] = Marks.nought
        self.fakeBoard.board[1][1] = Marks.nought
        self.fakeBoard.board[1][2] = Marks.cross
        self.fakeBoard.board[2][0] = Marks.nought
        self.fakeBoard.board[2][1] = Marks.cross
        self.fakeBoard.board[2][2] = Marks.nought
        self.fakeGamePolicy.responseWin = False
        self.fakeGamePolicy.responseCheckTie = True

        self.gameEngine.play()

        self.assertTrue(self.gameEngine.tie)
        self.assertTrue(self.gameEngine.gameOver)
        self.assertEqual(self.gameEngine.winner, None)

    def testPlay_whenPlayerSwitch(self):
        self.fakeGamePolicy.responseWin = False
        self.fakeGamePolicy.responseCheckTie = False
        fakePlayerOne = FakePlayer(Marks.cross)
        fakePlayerTwo = FakePlayer(Marks.nought)
        self.gameEngine.player1 = fakePlayerOne
        self.gameEngine.player2 = fakePlayerTwo
        self.gameEngine.currentPlayer = fakePlayerOne

        self.gameEngine.play()

        self.assertEqual(self.gameEngine.currentPlayer, fakePlayerTwo)

if __name__ == '__main__':
    unittest.main()
