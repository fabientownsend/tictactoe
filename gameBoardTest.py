import unittest

from gameBoard import GameBoard
from gameBoard import SpotNotEmpty

class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.gameBoard = GameBoard()

    def testCreateBoardTest(self):
        response = self.gameBoard.createBoard()
        expected = list('-'*9)
        self.assertEqual(response, expected)

    def testGetBoard_whenNewObject(self):
        self.gameBoard = GameBoard()
        response = self.gameBoard.getBoard()
        expected = list('-'*9)
        self.assertEqual(response, expected)

    def testSetMark_whenSpotIsEmpty(self):
        self.gameBoard.setMark(0)
        response = self.gameBoard.getBoard()
        expected = ['x', '-', '-', '-', '-', '-', '-', '-', '-']
        self.assertEqual(response, expected)

    def testSetMark_whenSpotNotFree(self):
        self.gameBoard.setMark(0)
        with self.assertRaises(SpotNotEmpty):
            self.gameBoard.setMark(0)

    def testSetMark_whenOutOfBoard(self):
        with self.assertRaises(IndexError):
            self.gameBoard.setMark(10)

if __name__ == '__main__':
    unittest.main()
