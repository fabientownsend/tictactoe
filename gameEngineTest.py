import unittest

from computer import Computer
from gameEngine import GameEngine
from gameEngine import PlayersEnum
from human import Human


class GameEngineTest(unittest.TestCase):
    def setUp(self):
        self.gameEngine = GameEngine()

    def testCreatePlayer_whenTwoHuman(self):
        self.gameEngine.createPlayers(1)
        self.assertTrue(isinstance(self.gameEngine.player1, Human))
        self.assertTrue(isinstance(self.gameEngine.player2, Human))

    def testCreatePlayer_whenHumanAndComputer(self):
        self.gameEngine.createPlayers(2)
        self.assertTrue(isinstance(self.gameEngine.player1, Human))
        self.assertTrue(isinstance(self.gameEngine.player2, Computer))

    def testCreatePlayer_whenTwoComputer(self):
        self.gameEngine.createPlayers(3)
        self.assertTrue(isinstance(self.gameEngine.player1, Computer))
        self.assertTrue(isinstance(self.gameEngine.player2, Computer))

    def testSetFirstPlayer_whenFirstPlayerIsPlayer1(self):
        self.gameEngine.createPlayers(1)
        self.gameEngine.setFirstPlayer(1)
        self.assertEqual(self.gameEngine.currentPlayer, self.gameEngine.player1)

    def testSetFirstPlayer_whenFirstPlayerIsPlayer2(self):
        self.gameEngine.createPlayers(2)
        self.gameEngine.setFirstPlayer(2)
        self.assertEqual(self.gameEngine.currentPlayer, self.gameEngine.player2)

    def testSwitchPlayer_whenCurrentPlayerWasPlayer1(self):
        self.gameEngine.createPlayers(2)
        self.gameEngine.currentPlayer = self.gameEngine.player1
        self.gameEngine.switchCurrentPlayer()
        self.assertEqual(self.gameEngine.currentPlayer, self.gameEngine.player2)

    def testSwitchPlayer_whenCurrentPlayerWasPlayer2(self):
        self.gameEngine.createPlayers(2)
        self.gameEngine.currentPlayer = self.gameEngine.player2
        self.gameEngine.switchCurrentPlayer()
        self.assertEqual(self.gameEngine.currentPlayer, self.gameEngine.player1)

    def testWin_whenItsNotWin(self):
        self.assertFalse(self.gameEngine.gameOver)

if __name__ == '__main__':
    unittest.main()
