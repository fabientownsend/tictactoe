import unittest

from computer import Computer
from fakeConsoleUI import FakeConsoleUI
from fakeGamePolicy import FakeGamePolicy
from gameEngine import GameEngine
from gameEngine import PlayersEnum
from human import Human


class GameEngineTest(unittest.TestCase):
    def setUp(self):
        self.fakeConsole = FakeConsoleUI()
        self.fakeGamePolicy = FakeGamePolicy()
        self.gameEngine = GameEngine(self.fakeConsole, self.fakeGamePolicy)

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
        response = self.gameEngine.getTypeGameSelected()
        self.assertEqual(response, 2)

    def testGetFirstPlayersSelected_whenFirstPlayerPlayer1(self):
        response = self.gameEngine.getFirstPlayerSlected()
        self.assertEqual(response, 1)

    def testIsGameOver_whenAPlayerWin(self):
        fakeBoard = None
        self.gameEngine.createPlayersTypeGame(2)
        self.gameEngine.setFirstPlayer(2)
        self.fakeGamePolicy.responseWin = True
        self.fakeGamePolicy.responseCheckTie = False

        response = self.gameEngine.isGameOver(fakeBoard)
        self.assertTrue(response)
        self.assertTrue(self.gameEngine.gameOver)
        self.assertFalse(self.gameEngine.tie)

    def testIsGameOver_whenItsATie(self):
        fakeBoard = None
        self.gameEngine.createPlayersTypeGame(2)
        self.gameEngine.setFirstPlayer(2)
        self.fakeGamePolicy.responseWin = False
        self.fakeGamePolicy.responseCheckTie = True

        response = self.gameEngine.isGameOver(fakeBoard)
        self.assertTrue(response)
        self.assertTrue(self.gameEngine.tie)
        self.assertTrue(self.gameEngine.gameOver)

    def testIsGameOver_whenItsNotGameOverNeitherTie(self):
        fakeBoard = None
        self.gameEngine.createPlayersTypeGame(2)
        self.gameEngine.setFirstPlayer(2)
        self.fakeGamePolicy.responseWin = False
        self.fakeGamePolicy.responseCheckTie = False

        response = self.gameEngine.isGameOver(fakeBoard)
        self.assertFalse(response)
        self.assertFalse(self.gameEngine.tie)
        self.assertFalse(self.gameEngine.gameOver)

    def testCreateTypeGame_whenCreateGameHumanVsComputer(self):
        self.gameEngine.createTypeGame()
        self.assertTrue(isinstance(self.gameEngine.player1, Human))
        self.assertTrue(isinstance(self.gameEngine.player2, Computer))

    def testDefineFirstPlayer(self):
        self.gameEngine.createTypeGame()
        self.gameEngine.defineFirstPlayer()
        self.assertEqual(self.gameEngine.currentPlayer, self.gameEngine.player1)

    def testDisplayResult_wheItsATie(self):
        self.gameEngine.tie = True
        self.gameEngine.displayResult()
        self.assertTrue(self.fakeConsole.passedIntoDisplayTie)

    def testDisplayResult_wheItsATie(self):
        self.gameEngine.createTypeGame()
        self.gameEngine.tie = False
        self.gameEngine.winner = self.gameEngine.player1
        self.gameEngine.displayResult()
        self.assertTrue(self.fakeConsole.passedIntoDisplayWinner)

if __name__ == '__main__':
    unittest.main()
