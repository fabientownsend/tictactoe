import unittest

from computer import Computer
from gameBoard import GameBoard
from marksEnum import Marks


class ComputerTest(unittest.TestCase):
    def setUp(self):
        self.computer = Computer(Marks.cross)

    def getEmptyBoard(self, boardSize):
        return [[Marks.empty]*boardSize for n in range(boardSize)]

    def testSetMark_whenMarkIsCrossse(self):
        self.computer = Computer(Marks.cross)
        self.assertEqual(self.computer.mark, Marks.cross)

    def testSetMark_whenMarkIsNought(self):
        self.computer = Computer(Marks.nought)
        self.assertEqual(self.computer.mark, Marks.nought)

    def testSwtich_whenMarkWasCross(self):
        response = self.computer.switch(Marks.cross)
        self.assertEqual(response, Marks.nought)

    def testSwtich_whenMarkWasNought(self):
        response = self.computer.switch(Marks.nought)
        self.assertEqual(response, Marks.cross)

    def testMinimax_whenMaximizingPlayerWin(self):
        maximizingPlayer = Marks.cross
        self.gameBoard = GameBoard(3)
        self.gameBoard.board[0][0] = Marks.cross
        self.gameBoard.board[0][1] = Marks.cross
        self.gameBoard.board[0][2] = Marks.cross

        response = self.computer.minimax(maximizingPlayer, self.gameBoard)
        self.assertEqual(response, 1)

    def testMinimax_whenMinimizinglayerWin(self):
        maximizingPlayer = Marks.cross
        self.gameBoard = GameBoard(3)
        self.gameBoard.board[0][0] = Marks.nought
        self.gameBoard.board[0][1] = Marks.nought
        self.gameBoard.board[0][2] = Marks.nought

        response = self.computer.minimax(maximizingPlayer, self.gameBoard)
        self.assertEqual(response, -1)

    def testMinimax_whenItsTie(self):
        maximizingPlayer = Marks.cross
        self.gameBoard = GameBoard(3)
        self.gameBoard.board[0][0] = Marks.nought
        self.gameBoard.board[0][1] = Marks.cross
        self.gameBoard.board[0][2] = Marks.nought
        self.gameBoard.board[1][0] = Marks.nought
        self.gameBoard.board[1][1] = Marks.cross
        self.gameBoard.board[1][2] = Marks.cross
        self.gameBoard.board[2][0] = Marks.cross
        self.gameBoard.board[2][1] = Marks.nought
        self.gameBoard.board[2][2] = Marks.cross

        response = self.computer.minimax(maximizingPlayer, self.gameBoard)
        self.assertEqual(response, 0)

    def testMinimax_whenMaximizingPlayerUltimateWhin(self):
        maximizingPlayer = Marks.nought
        self.gameBoard = GameBoard(3)
        self.gameBoard.board[0][0] = Marks.empty
        self.gameBoard.board[0][1] = Marks.cross
        self.gameBoard.board[0][2] = Marks.nought
        self.gameBoard.board[1][0] = Marks.empty
        self.gameBoard.board[1][1] = Marks.cross
        self.gameBoard.board[1][2] = Marks.cross
        self.gameBoard.board[2][0] = Marks.nought
        self.gameBoard.board[2][1] = Marks.nought
        self.gameBoard.board[2][2] = Marks.cross

        response = self.computer.minimax(maximizingPlayer, self.gameBoard)
        self.assertEqual(response, 1)

    def testMinimax_whenMinimizingPlayerUltimateWhin(self):
        maximizingPlayer = Marks.cross
        self.gameBoard = GameBoard(3)
        self.gameBoard.board[0][0] = Marks.empty
        self.gameBoard.board[0][1] = Marks.nought
        self.gameBoard.board[0][2] = Marks.cross
        self.gameBoard.board[1][0] = Marks.empty
        self.gameBoard.board[1][1] = Marks.nought
        self.gameBoard.board[1][2] = Marks.nought
        self.gameBoard.board[2][0] = Marks.cross
        self.gameBoard.board[2][1] = Marks.cross
        self.gameBoard.board[2][2] = Marks.nought

        response = self.computer.minimax(maximizingPlayer, self.gameBoard)
        self.assertEqual(response, -1)

    def testGetMove_whenItCanWin(self):
        maximizingPlayer = Marks.cross
        self.gameBoard = GameBoard(3)
        self.gameBoard.board[0][0] = Marks.cross
        self.gameBoard.board[0][1] = Marks.cross
        self.gameBoard.board[0][2] = Marks.empty
        self.gameBoard.board[1][0] = Marks.empty
        self.gameBoard.board[1][1] = Marks.empty
        self.gameBoard.board[1][2] = Marks.empty
        self.gameBoard.board[2][0] = Marks.empty
        self.gameBoard.board[2][1] = Marks.empty
        self.gameBoard.board[2][2] = Marks.nought

        response = self.computer.getMove(self.gameBoard)
        self.assertEqual(response, 2)

    def testGetMove_whenItShouldBlockTheAdversaire(self):
        maximizingPlayer = Marks.cross
        self.gameBoard = GameBoard(3)
        self.gameBoard.board[0][0] = Marks.nought
        self.gameBoard.board[0][1] = Marks.nought
        self.gameBoard.board[0][2] = Marks.empty
        self.gameBoard.board[1][0] = Marks.empty
        self.gameBoard.board[1][1] = Marks.empty
        self.gameBoard.board[1][2] = Marks.empty
        self.gameBoard.board[2][0] = Marks.empty
        self.gameBoard.board[2][1] = Marks.empty
        self.gameBoard.board[2][2] = Marks.nought

        response = self.computer.getMove(self.gameBoard)
        self.assertEqual(response, 2)

    def testGetMove_whenCanHaveAnUltimateWin(self):
        maximizingPlayer = Marks.cross
        self.gameBoard = GameBoard(3)
        self.gameBoard.board[0][0] = Marks.cross
        self.gameBoard.board[0][1] = Marks.nought
        self.gameBoard.board[0][2] = Marks.empty
        self.gameBoard.board[1][0] = Marks.cross
        self.gameBoard.board[1][1] = Marks.empty
        self.gameBoard.board[1][2] = Marks.empty
        self.gameBoard.board[2][0] = Marks.nought
        self.gameBoard.board[2][1] = Marks.empty
        self.gameBoard.board[2][2] = Marks.empty

        response = self.computer.getMove(self.gameBoard)
        self.assertEqual(response, 4)

if __name__ == '__main__':
    unittest.main()
