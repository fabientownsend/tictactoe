import unittest

from game_board import GameBoard
from marks_enum import Marks


class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.boardSize = 3
        self.gameBoard = GameBoard(self.boardSize)
        self.newGameBoard = self.gameBoard.create_board()

    def getEmptyBoard(self, boardSize):
        return [[Marks.empty]*boardSize for n in range(boardSize)]

    def testCreateBoardTest_whenBoardThreeByThree(self):
        emptyGameBoard = self.getEmptyBoard(self.boardSize)
        self.assertEqual(self.newGameBoard, emptyGameBoard)

    def testCreateBoardTest_whenBoardFourByFour(self):
        boardSize = 4
        emptyGameBoard = self.getEmptyBoard(boardSize)
        gameBoard = GameBoard(boardSize)
        newGameBoard = gameBoard.create_board()
        self.assertEqual(newGameBoard, emptyGameBoard)

    def testSetMark_whenSpotIsEmpty(self):
        position = 0
        self.gameBoard.set_mark(position, Marks.cross)
        markSetOnBoard = self.gameBoard.get_mark(position)
        self.assertEqual(Marks.cross, markSetOnBoard)

    def testSetMark_whenOutOfBoard(self):
        position = 10
        with self.assertRaises(IndexError):
            self.gameBoard.set_mark(position, Marks.cross)

    def testIsEmpty_whenSpotIsEmpty(self):
        position = 0
        self.gameBoard.set_mark(position, Marks.cross)
        self.assertFalse(self.gameBoard.is_empty(position))

if __name__ == '__main__':
    unittest.main()
