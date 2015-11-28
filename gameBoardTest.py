import unittest

from gameBoard import GameBoard
from gameBoard import SpotNotEmpty

class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.gameBoard = GameBoard()

    def getEmptyBoard(self):
        return list('-'*9)

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
        self.gameBoard.setMark(5)
        response = self.gameBoard.isFree(5)
        self.assertEqual(response, False)

    def testResetBoard_whenBoardEmpty(self):
        self.gameBoard.setMark(5)
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

    def testCheckLines_whenLineOneWin(self):
        self.gameBoard.setMark(0)
        self.gameBoard.setMark(1)
        self.gameBoard.setMark(2)
        self.assertEqual(self.gameBoard.checkLines(), True)

    def testCheckLines_whenLineTwoWin(self):
        self.gameBoard.setMark(3)
        self.gameBoard.setMark(4)
        self.gameBoard.setMark(5)
        self.assertEqual(self.gameBoard.checkLines(), True)

    def testCheckLines_whenLineThreeWin(self):
        self.gameBoard.setMark(6)
        self.gameBoard.setMark(7)
        self.gameBoard.setMark(8)
        self.assertEqual(self.gameBoard.checkLines(), True)

    def testCheckLines_whenEmpty(self):
        self.gameBoard.resetBoard()
        self.assertEqual(self.gameBoard.checkLines(), False)

    def testCheckColumns_whenColumnsOneWin(self):
        self.gameBoard.setMark(0)
        self.gameBoard.setMark(3)
        self.gameBoard.setMark(6)
        self.assertEqual(self.gameBoard.checkColumns(), True)

    def testCheckColumns_whenColumnsTwoWin(self):
        self.gameBoard.setMark(1)
        self.gameBoard.setMark(4)
        self.gameBoard.setMark(7)
        self.assertEqual(self.gameBoard.checkColumns(), True)

    def testCheckColumns_whenColumnsThreeWin(self):
        self.gameBoard.setMark(2)
        self.gameBoard.setMark(5)
        self.gameBoard.setMark(8)
        self.assertEqual(self.gameBoard.checkColumns(), True)

    def testCheckColumns_whenEmpty(self):
        self.gameBoard.resetBoard()
        self.assertEqual(self.gameBoard.checkColumns(), False)

    def testCheckDiagonals_whenDialOneWin(self):
        self.gameBoard.setMark(0)
        self.gameBoard.setMark(4)
        self.gameBoard.setMark(8)
        self.assertEqual(self.gameBoard.checkDiagonals(), True)

    def testCheckDiagonals_whenDialTwoWin(self):
        self.gameBoard.setMark(2)
        self.gameBoard.setMark(4)
        self.gameBoard.setMark(6)
        self.assertEqual(self.gameBoard.checkDiagonals(), True)

    def testCheckDiagonals_whenEmpty(self):
        self.gameBoard.resetBoard()
        self.assertEqual(self.gameBoard.checkDiagonals(), False)

    def testWin_whenLineOneWin(self):
        self.gameBoard.setMark(0)
        self.gameBoard.setMark(1)
        self.gameBoard.setMark(2)
        self.assertEqual(self.gameBoard.win(), True)

    def testWin_whenLineTwoWin(self):
        self.gameBoard.setMark(3)
        self.gameBoard.setMark(4)
        self.gameBoard.setMark(5)
        self.assertEqual(self.gameBoard.win(), True)

    def testWin_whenLineThreeWin(self):
        self.gameBoard.setMark(6)
        self.gameBoard.setMark(7)
        self.gameBoard.setMark(8)
        self.assertEqual(self.gameBoard.win(), True)

    def testWin_whenColumnsOneWin(self):
        self.gameBoard.setMark(0)
        self.gameBoard.setMark(3)
        self.gameBoard.setMark(6)
        self.assertEqual(self.gameBoard.win(), True)

    def testWin_whenColumnsTwoWin(self):
        self.gameBoard.setMark(1)
        self.gameBoard.setMark(4)
        self.gameBoard.setMark(7)
        self.assertEqual(self.gameBoard.win(), True)

    def testWin_whenColumnsThreeWin(self):
        self.gameBoard.setMark(2)
        self.gameBoard.setMark(5)
        self.gameBoard.setMark(8)
        self.assertEqual(self.gameBoard.win(), True)

    def testWin_whenDialOneWin(self):
        self.gameBoard.setMark(0)
        self.gameBoard.setMark(4)
        self.gameBoard.setMark(8)
        self.assertEqual(self.gameBoard.win(), True)

    def testWin_whenDialTwoWin(self):
        self.gameBoard.setMark(2)
        self.gameBoard.setMark(4)
        self.gameBoard.setMark(6)
        self.assertEqual(self.gameBoard.win(), True)

if __name__ == '__main__':
    unittest.main()
