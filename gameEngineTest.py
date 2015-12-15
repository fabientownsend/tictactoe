from gameEngine import GameEngine
from gameEngine import PlayersEnum
from gameEngine import GameTypeNotExist
from gameEngine import GameTypeNotExist
from computer import Computer
from human import Human
import unittest

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

    def testCreatePlayer_whenTypePartyDoNotExist(self):
        with self.assertRaises(GameTypeNotExist):
            self.gameEngine.createPlayers(4)

    def testSetFirstPlayer_whenFirstPlayerIsPlayer1(self):
        self.gameEngine.createPlayers(1)
        self.gameEngine.setFirstPlayer(PlayersEnum.player1)
        self.assertEqual(self.gameEngine.currentPlayer, self.gameEngine.player1)

    def testSetFirstPlayer_whenFirstPlayerIsPlayer2(self):
        self.gameEngine.createPlayers(2)
        self.gameEngine.setFirstPlayer(PlayersEnum.player2)
        self.assertEqual(self.gameEngine.currentPlayer, self.gameEngine.player2)

    def testSwitchPlayer_whenCurrentPlayerWasPlayer1(self):
        self.gameEngine.createPlayers(2)
        self.gameEngine.currentPlayer = self.gameEngine.player1
        self.gameEngine.switchCurrentPlayer()
        self.assertEqual(self.gameEngine.currentPlayer, self.gameEngine.player2)

    def testSwitchPlayer_whenCurrentPlayerWasPlayer2(self):
        self.gameEngine.createPlayers(2)
        self.gameEngine.currentPlayer = self.gameEngine.player1
        self.gameEngine.switchCurrentPlayer()
        self.assertEqual(self.gameEngine.currentPlayer, self.gameEngine.player2)

if __name__ == '__main__':
    unittest.main()
