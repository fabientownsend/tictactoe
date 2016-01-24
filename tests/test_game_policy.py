import unittest

from game_policy import GamePolicy
from marks_enum import Marks


class GamePolicyTest(unittest.TestCase):
    def setUp(self):
        self.gamePolicy = GamePolicy()

    def getEmptyBoardSize(self, boardSize):
        return [[Marks.empty]*boardSize for n in range(boardSize)]

    def testIsFull_whenItsEmpty(self):
        emptyBoard = self.getEmptyBoardSize(3)
        self.assertFalse(self.gamePolicy.is_full(emptyBoard))

    def testIsFull_whenItsNotEmpty(self):
        board = self.getEmptyBoardSize(3)
        board[0][0] = Marks.cross
        self.assertFalse(self.gamePolicy.is_full(board))

    def testWin_whenRowsAreWin(self):
        mark = Marks.cross
        board = self.getEmptyBoardSize(3)

        for row in range(len(board)):
            board = self.setMarkRow(board, mark, row)

            self.assertTrue(self.gamePolicy.row_win(row, board, mark))
            self.assertTrue(self.gamePolicy.win(board, Marks.cross))

    def setMarkRow(self, board, mark, row):
        for column in range(len(board)):
            board[row][column] = mark

        return board

    def testWin_whenColumnsAreWin(self):
        mark = Marks.cross
        board = self.getEmptyBoardSize(3)

        for column in range(len(board)):
            board = self.setMarkColumn(board, mark, column)

            self.assertTrue(self.gamePolicy.column_win(column, board, mark))
            self.assertTrue(self.gamePolicy.win(board, Marks.cross))

    def setMarkColumn(self, board, mark, column):
        for row in range(len(board)):
            board[row][column] = mark

        return board

    def testWin_whenDialOneWin(self):
        diagonal = 0
        boardSize = 3
        mark = Marks.cross
        board = self.getEmptyBoardSize(boardSize)

        for position in range(boardSize):
            board[position][position] = mark

        self.assertTrue(self.gamePolicy.diagonal_win(diagonal, board, mark))
        self.assertTrue(self.gamePolicy.win(board, mark))

    def testWin_whenDialTwoWin(self):
        diagonal = 1
        boardSize = 3
        mark = Marks.cross
        board = self.getEmptyBoardSize(boardSize)

        for position in range(boardSize):
            board[position][boardSize - position - 1] = mark

        self.assertTrue(self.gamePolicy.diagonal_win(diagonal, board, mark))
        self.assertTrue(self.gamePolicy.win(board, mark))

    def testCheckTie_whenItsTie(self):
        board = self.getEmptyBoardSize(3)
        board[0][0] = Marks.cross
        board[0][1] = Marks.nought
        board[0][2] = Marks.cross
        board[1][0] = Marks.nought
        board[1][1] = Marks.nought
        board[1][2] = Marks.cross
        board[2][0] = Marks.nought
        board[2][1] = Marks.cross
        board[2][2] = Marks.nought

        self.assertTrue(self.gamePolicy.check_tie(board))

    def testCheckTie_whenBoardIsNotFull(self):
        board = self.getEmptyBoardSize(3)
        board[0][0] = Marks.cross
        board[0][1] = Marks.nought
        board[0][2] = Marks.cross
        board[1][0] = Marks.empty
        board[1][1] = Marks.nought
        board[1][2] = Marks.cross
        board[2][0] = Marks.nought
        board[2][1] = Marks.cross
        board[2][2] = Marks.nought

        self.assertFalse(self.gamePolicy.check_tie(board))

    def testCheckTie_whenItsNotTieButWin(self):
        board = self.getEmptyBoardSize(3)
        board[0][0] = Marks.cross
        board[0][1] = Marks.cross
        board[0][2] = Marks.cross
        board[1][0] = Marks.cross
        board[1][1] = Marks.cross
        board[1][2] = Marks.cross
        board[2][0] = Marks.cross
        board[2][1] = Marks.cross
        board[2][2] = Marks.cross

        self.assertFalse(self.gamePolicy.check_tie(board))

if __name__ == '__main__':
    unittest.main()
