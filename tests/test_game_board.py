import unittest

from gameBoard import GameBoard
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
        emptyGameBoard = self.getEmptyBoard(boardSize)
        gameBoard = GameBoard(boardSize)
        newGameBoard = gameBoard.createBoard()
        self.assertEqual(newGameBoard, emptyGameBoard)

    def testSetMark_whenSpotIsEmpty(self):
        position = 0
        self.gameBoard.setMark(position, Marks.cross)
        markSetOnBoard = self.gameBoard.getMark(position)
        self.assertEqual(Marks.cross, markSetOnBoard)

    def testSetMark_whenOutOfBoard(self):
        position = 10
        with self.assertRaises(IndexError):
            self.gameBoard.setMark(position, Marks.cross)

    def testIsEmpty_whenSpotIsEmpty(self):
        position = 0
        self.gameBoard.setMark(position, Marks.cross)
        self.assertFalse(self.gameBoard.isEmpty(position))

if __name__ == '__main__':
    unittest.main()
