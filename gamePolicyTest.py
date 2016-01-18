import unittest

from gamePolicy import GamePolicy
from marksEnum import Marks


class GamePolicyTest(unittest.TestCase):
    def setUp(self):
        self.gamePolicy = GamePolicy()

    def getEmptyBoard(self, boardSize):
        return [[Marks.empty]*boardSize for n in range(boardSize)]

    def testIsEmpty_whenItsEmpty(self):
        emptyBoard = self.getEmptyBoard(3)
        self.assertTrue(self.gamePolicy.isEmpty(emptyBoard))

    def testIsEmpty_whenItsNotEmpty(self):
        board = self.getEmptyBoard(3)
        board[0][0] = Marks.cross
        self.assertFalse(self.gamePolicy.isEmpty(board))

    def testWin_whenLineOneWin(self):
        boardSize = 3
        rowOne = 0
        board = self.getEmptyBoard(boardSize)
        for column in range(boardSize):
            board[rowOne][column] = Marks.cross

        isWinningRow = self.gamePolicy.rowMarked(rowOne, board, Marks.cross)
        isWinningBoard = self.gamePolicy.win(board, Marks.cross)
        self.assertTrue(isWinningRow)
        self.assertTrue(isWinningBoard)

    def testWin_whenLineTwoWin(self):
        boardSize = 3
        rowTwo = 1
        board = self.getEmptyBoard(boardSize)
        for column in range(boardSize):
            board[rowTwo][column] = Marks.cross

        isWinningRow = self.gamePolicy.rowMarked(rowTwo, board, Marks.cross)
        isWinningBoard = self.gamePolicy.win(board, Marks.cross)
        self.assertTrue(isWinningRow)
        self.assertTrue(isWinningBoard)

    def testWin_whenLineThreeWin(self):
        boardSize = 3
        rowThree = 2
        board = self.getEmptyBoard(boardSize)
        for column in range(boardSize):
            board[rowThree][column] = Marks.cross

        isWinningRow = self.gamePolicy.rowMarked(rowThree, board, Marks.cross)
        isWinningBoard = self.gamePolicy.win(board, Marks.cross)
        self.assertTrue(isWinningRow)
        self.assertTrue(isWinningBoard)

    def testWin_whenColumnsOneWin(self):
        boardSize = 3
        columnOne = 0
        board = self.getEmptyBoard(boardSize)
        for row in range(boardSize):
            board[row][columnOne] = Marks.cross

        isWinningColumn = self.gamePolicy.columnMarked(columnOne, board, Marks.cross)
        isWinningBoard = self.gamePolicy.win(board, Marks.cross)
        self.assertTrue(isWinningColumn)
        self.assertTrue(isWinningBoard)

    def testWin_whenColumnsTwoWin(self):
        boardSize = 3
        columnTwo = 1
        board = self.getEmptyBoard(boardSize)
        for row in range(boardSize):
            board[row][columnTwo] = Marks.cross

        isWinningColumn = self.gamePolicy.columnMarked(columnTwo, board, Marks.cross)
        isWinningBoard = self.gamePolicy.win(board, Marks.cross)
        self.assertTrue(isWinningColumn)
        self.assertTrue(isWinningBoard)

    def testWin_whenColumnsThreeWin(self):
        boardSize = 3
        columnThree = 2
        board = self.getEmptyBoard(boardSize)
        for row in range(boardSize):
            board[row][columnThree] = Marks.cross

        isWinningColumn = self.gamePolicy.columnMarked(columnThree, board, Marks.cross)
        isWinningBoard = self.gamePolicy.win(board, Marks.cross)
        self.assertTrue(isWinningColumn)
        self.assertTrue(isWinningBoard)

    def testWin_whenDialOneWin(self):
        boardSize = 3
        diagonal = 0
        board = self.getEmptyBoard(boardSize)
        for position in range(boardSize):
            board[position][position] = Marks.cross

        isWinningDiagonal = self.gamePolicy.diagonalMarked(diagonal, board, Marks.cross)
        isWinningBoard = self.gamePolicy.win(board, Marks.cross)
        self.assertTrue(isWinningDiagonal)
        self.assertTrue(isWinningBoard)

    def testWin_whenDialTwoWin(self):
        boardSize = 3
        diagonal = 1
        board = self.getEmptyBoard(boardSize)
        for position in range(boardSize):
            board[position][boardSize - position - 1] = Marks.cross

        isWinningDiagonal = self.gamePolicy.diagonalMarked(diagonal, board, Marks.cross)
        isWinningBoard = self.gamePolicy.win(board, Marks.cross)
        self.assertTrue(isWinningDiagonal)
        self.assertTrue(isWinningBoard)

    def testCheckTie_whenItsTie(self):
        boardSize = 3
        board = self.getEmptyBoard(boardSize)
        board[0][0] = Marks.cross
        board[0][1] = Marks.nought
        board[0][2] = Marks.cross
        board[1][0] = Marks.nought
        board[1][1] = Marks.nought
        board[1][2] = Marks.cross
        board[2][0] = Marks.nought
        board[2][1] = Marks.cross
        board[2][2] = Marks.nought

        response = self.gamePolicy.checkTie(board)
        self.assertTrue(response)

    def testCheckTie_whenItsNotTieButWin(self):
        boardSize = 3
        board = self.getEmptyBoard(boardSize)
        board[0][0] = Marks.cross
        board[0][1] = Marks.cross
        board[0][2] = Marks.cross
        board[1][0] = Marks.cross
        board[1][1] = Marks.empty
        board[1][2] = Marks.cross
        board[2][0] = Marks.cross
        board[2][1] = Marks.cross
        board[2][2] = Marks.cross

        response = self.gamePolicy.checkTie(board)
        self.assertFalse(response)


if __name__ == '__main__':
    unittest.main()
