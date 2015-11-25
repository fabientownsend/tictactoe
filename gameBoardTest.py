import unittest
from gameBoard import GameBoard

class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.gameBoard = GameBoard()

    def testNewBoardTest(self):
        response = self.gameBoard.newBoard()
        expected = list("-"*9)
        self.assertEqual(response, expected)

if __name__ == '__main__':
    unittest.main()
