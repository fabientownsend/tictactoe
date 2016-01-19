import unittest

from gameBoard import GameBoard
from gameBoard import SpotNotEmpty
from marksEnum import Marks


class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.boardSize = 3
        self.gameBoard = GameBoard(self.boardSize)
        self.newGameBoard = self.gameBoard.createBoard()

    def getEmptyBoard(self, boardSize):
        return [[Marks.empty]*boardSize for n in range(boardSize)]

    def testCreateBoardTest_whenBoardThreeByThree(self):
        emptyGameBoard = self.getEmptyBoard(self.boardSize)
        self.assertEqual(self.newGameBoard, emptyGameBoard)

    def testCreateBoardTest_whenBoardFourByFour(self):
        boardSize = 4
        gameBoard = GameBoard(boardSize)
        newGameBoard = gameBoard.createBoard()
        emptyGameBoard = self.getEmptyBoard(boardSize)
        self.assertEqual(newGameBoard, emptyGameBoard)

    def testSetMark_whenSpotIsEmpty(self):
        mark = Marks.cross
        self.gameBoard.setMark(0, mark)
        markSetOnBoard = self.gameBoard.getMark(0)
        self.assertEqual(mark, markSetOnBoard)

    def testSetMark_whenSpotNotFree(self):
        mark = Marks.cross
        self.gameBoard.setMark(0, Marks.cross)
        with self.assertRaises(SpotNotEmpty):
            self.gameBoard.setMark(0, Marks.cross)

    def testSetMark_whenOutOfBoard(self):
        mark = Marks.cross
        with self.assertRaises(IndexError):
            self.gameBoard.setMark(10, Marks.cross)

    def testIsEmpty_whenSpotIsEmpty(self):
        mark = Marks.cross
        position = 0
        self.gameBoard.setMark(position, mark)
        self.assertFalse(self.gameBoard.isEmpty(position))

if __name__ == '__main__':
    unittest.main()
