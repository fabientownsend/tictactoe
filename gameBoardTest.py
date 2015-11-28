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

    def testIsFree_whenSpotFree(self):
        self.gameBoard.resetBoard()
        response = self.gameBoard.isFree(5)
        self.assertEqual(response, True)

    def testIsFree_whenSpotNotFree(self):
        self.gameBoard.resetBoard()
        self.gameBoard.setMark(5, Marks.cross)
        response = self.gameBoard.isFree(5)
        self.assertEqual(response, False)

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

    def testCheckLines_whenLineOneWin(self):
        self.gameBoard.setMark(0, Marks.cross)
        self.gameBoard.setMark(1, Marks.cross)
        self.gameBoard.setMark(2, Marks.cross)
        response = self.gameBoard.checkLines(Marks.cross)
        self.assertEqual(response, True)

    def testCheckLines_whenLineTwoWin(self):
        self.gameBoard.setMark(3, Marks.cross)
        self.gameBoard.setMark(4, Marks.cross)
        self.gameBoard.setMark(5, Marks.cross)
        response = self.gameBoard.checkLines(Marks.cross)
        self.assertEqual(response, True)

    def testCheckLines_whenLineThreeWin(self):
        self.gameBoard.setMark(6, Marks.cross)
        self.gameBoard.setMark(7, Marks.cross)
        self.gameBoard.setMark(8, Marks.cross)
        response = self.gameBoard.checkLines(Marks.cross)
        self.assertEqual(response, True)

    def testCheckLines_whenEmpty(self):
        self.gameBoard.resetBoard()
        response = self.gameBoard.checkLines(Marks.cross)
        self.assertEqual(response, False)

    def testCheckColumns_whenColumnsOneWin(self):
        self.gameBoard.setMark(0, Marks.cross)
        self.gameBoard.setMark(3, Marks.cross)
        self.gameBoard.setMark(6, Marks.cross)
        response = self.gameBoard.checkColumns(Marks.cross)
        self.assertEqual(response, True)

    def testCheckColumns_whenColumnsTwoWin(self):
        self.gameBoard.setMark(1, Marks.cross)
        self.gameBoard.setMark(4, Marks.cross)
        self.gameBoard.setMark(7, Marks.cross)
        response = self.gameBoard.checkColumns(Marks.cross)
        self.assertEqual(response, True)

    def testCheckColumns_whenColumnsThreeWin(self):
        self.gameBoard.setMark(2, Marks.cross)
        self.gameBoard.setMark(5, Marks.cross)
        self.gameBoard.setMark(8, Marks.cross)
        response = self.gameBoard.checkColumns(Marks.cross)
        self.assertEqual(response, True)

    def testCheckColumns_whenEmpty(self):
        self.gameBoard.resetBoard()
        response = self.gameBoard.checkColumns(Marks.cross)
        self.assertEqual(response, False)

    def testCheckDiagonals_whenDialOneWin(self):
        self.gameBoard.setMark(0, Marks.cross)
        self.gameBoard.setMark(4, Marks.cross)
        self.gameBoard.setMark(8, Marks.cross)
        response = self.gameBoard.checkDiagonals(Marks.cross)
        self.assertEqual(response, True)

    def testCheckDiagonals_whenDialTwoWin(self):
        self.gameBoard.setMark(2, Marks.cross)
        self.gameBoard.setMark(4, Marks.cross)
        self.gameBoard.setMark(6, Marks.cross)
        response = self.gameBoard.checkDiagonals(Marks.cross)
        self.assertEqual(response, True)

    def testCheckDiagonals_whenEmpty(self):
        self.gameBoard.resetBoard()
        response = self.gameBoard.checkDiagonals(Marks.cross)
        self.assertEqual(response, False)

    def testWin_whenLineOneWin(self):
        self.gameBoard.setMark(0, Marks.cross)
        self.gameBoard.setMark(1, Marks.cross)
        self.gameBoard.setMark(2, Marks.cross)
        response = self.gameBoard.win(Marks.cross)
        self.assertEqual(response, True)

    def testWin_whenLineTwoWin(self):
        self.gameBoard.setMark(3, Marks.cross)
        self.gameBoard.setMark(4, Marks.cross)
        self.gameBoard.setMark(5, Marks.cross)
        response = self.gameBoard.win(Marks.cross)
        self.assertEqual(response, True)

    def testWin_whenLineThreeWin(self):
        self.gameBoard.setMark(6, Marks.cross)
        self.gameBoard.setMark(7, Marks.cross)
        self.gameBoard.setMark(8, Marks.cross)
        response = self.gameBoard.win(Marks.cross)
        self.assertEqual(response, True)

    def testWin_whenColumnsOneWin(self):
        self.gameBoard.setMark(0, Marks.cross)
        self.gameBoard.setMark(3, Marks.cross)
        self.gameBoard.setMark(6, Marks.cross)
        response = self.gameBoard.win(Marks.cross)
        self.assertEqual(response, True)

    def testWin_whenColumnsTwoWin(self):
        self.gameBoard.setMark(1, Marks.cross)
        self.gameBoard.setMark(4, Marks.cross)
        self.gameBoard.setMark(7, Marks.cross)
        response = self.gameBoard.win(Marks.cross)
        self.assertEqual(response, True)

    def testWin_whenColumnsThreeWin(self):
        self.gameBoard.setMark(2, Marks.cross)
        self.gameBoard.setMark(5, Marks.cross)
        self.gameBoard.setMark(8, Marks.cross)
        response = self.gameBoard.win(Marks.cross)
        self.assertEqual(response, True)

    def testWin_whenDialOneWin(self):
        self.gameBoard.setMark(0, Marks.cross)
        self.gameBoard.setMark(4, Marks.cross)
        self.gameBoard.setMark(8, Marks.cross)
        response = self.gameBoard.win(Marks.cross)
        self.assertEqual(response, True)

    def testWin_whenDialTwoWin(self):
        self.gameBoard.setMark(2, Marks.cross)
        self.gameBoard.setMark(4, Marks.cross)
        self.gameBoard.setMark(6, Marks.cross)
        response = self.gameBoard.win(Marks.cross)
        self.assertEqual(response, True)

if __name__ == '__main__':
    unittest.main()
