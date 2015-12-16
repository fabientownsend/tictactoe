import unittest

from gameBoard import GameBoard
from gameBoard import SpotNotEmpty
from marksEnum import Marks


class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.gameBoard = GameBoard()

    def getEmptyBoard(self):
        return [
            Marks.empty, Marks.empty, Marks.empty,
            Marks.empty, Marks.empty, Marks.empty,
            Marks.empty, Marks.empty, Marks.empty
        ]

    def testCreateBoardTest(self):
        response = self.gameBoard.createBoard()
        expected = self.getEmptyBoard()
        self.assertEqual(response, expected)

    def testResetBoard_whenBoardEmpty(self):
        self.gameBoard.setMark(5, Marks.cross)
        self.gameBoard.resetBoard()
        response = self.gameBoard.getBoard()
        expected = self.getEmptyBoard()
        self.assertEqual(response, expected)

    def testResetBoard_whenBoardNotEmpty(self):
        self.gameBoard.resetBoard()
        response = self.gameBoard.getBoard()
        expected = self.getEmptyBoard()
        self.assertEqual(response, expected)

    def testGetBoard_whenNewObject(self):
        self.gameBoard = GameBoard()
        response = self.gameBoard.getBoard()
        expected = self.getEmptyBoard()
        self.assertEqual(response, expected)

    def testSetMark_whenSpotIsEmpty(self):
        self.gameBoard.setMark(0, Marks.cross)
        response = self.gameBoard.getBoard()
        expected = [
            Marks.cross, Marks.empty, Marks.empty,
            Marks.empty, Marks.empty, Marks.empty,
            Marks.empty, Marks.empty, Marks.empty
        ]
        self.assertEqual(response, expected)

    def testSetMark_whenSpotNotFree(self):
        self.gameBoard.setMark(0, Marks.cross)
        with self.assertRaises(SpotNotEmpty):
            self.gameBoard.setMark(0, Marks.cross)

    def testSetMark_whenOutOfBoard(self):
        with self.assertRaises(IndexError):
            self.gameBoard.setMark(10, Marks.cross)

if __name__ == '__main__':
    unittest.main()
