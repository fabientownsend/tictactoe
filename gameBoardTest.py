import unittest
from gameBoard import GameBoard

class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.gameBoard = GameBoard()

    def testCreateBoardTest(self):
        response = self.gameBoard.createBoard()
        expected = list("-"*9)
        self.assertEqual(response, expected)

    def testGetBoard_whenNewObject(self):
        self.gameBoard = GameBoard()
        response = self.gameBoard.getBoard()
        expected = list("-"*9)
        self.assertEqual(response, expected)

if __name__ == '__main__':
    unittest.main()
