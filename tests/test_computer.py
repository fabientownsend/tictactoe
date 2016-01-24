import unittest

from computer import Computer
from game_board import GameBoard
from marks_enum import Marks


class ComputerTest(unittest.TestCase):
    def setUp(self):
        self.computer = Computer(Marks.cross)

    def testSetMark_whenMarkIsCross(self):
        self.computer = Computer(Marks.cross)
        self.assertEqual(self.computer.mark, Marks.cross)

    def testSetMark_whenMarkIsNought(self):
        self.computer = Computer(Marks.nought)
        self.assertEqual(self.computer.mark, Marks.nought)

    def testSwtich_whenMarkWasCross(self):
        noughtMark = self.computer.switch(Marks.cross)
        self.assertEqual(noughtMark, Marks.nought)

    def testSwtich_whenMarkWasNought(self):
        crassMark = self.computer.switch(Marks.nought)
        self.assertEqual(crassMark, Marks.cross)

    def testMinimax_whenMaximizingPlayerWin(self):
        maximizingPlayer = Marks.cross
        self.gameBoard = GameBoard(3)
        self.gameBoard.set_mark(0, Marks.cross)
        self.gameBoard.set_mark(1, Marks.cross)
        self.gameBoard.set_mark(2, Marks.cross)

        winMove = self.computer.minimax(maximizingPlayer, self.gameBoard)
        self.assertEqual(winMove, 1)

    def testMinimax_whenMinimizinglayerWin(self):
        maximizingPlayer = Marks.cross
        self.gameBoard = GameBoard(3)
        self.gameBoard.set_mark(0, Marks.nought)
        self.gameBoard.set_mark(1, Marks.nought)
        self.gameBoard.set_mark(2, Marks.nought)

        loseMove = self.computer.minimax(maximizingPlayer, self.gameBoard)
        self.assertEqual(loseMove, -1)

    def testMinimax_whenItsTie(self):
        maximizingPlayer = Marks.cross
        self.gameBoard = GameBoard(3)
        self.gameBoard.set_mark(0, Marks.nought)
        self.gameBoard.set_mark(1, Marks.cross)
        self.gameBoard.set_mark(2, Marks.nought)
        self.gameBoard.set_mark(3, Marks.nought)
        self.gameBoard.set_mark(4, Marks.cross)
        self.gameBoard.set_mark(5, Marks.cross)
        self.gameBoard.set_mark(6, Marks.cross)
        self.gameBoard.set_mark(7, Marks.nought)
        self.gameBoard.set_mark(8, Marks.cross)

        tieMove = self.computer.minimax(maximizingPlayer, self.gameBoard)
        self.assertEqual(tieMove, 0)

    def testMinimax_whenMaximizingPlayerUltimateWhin(self):
        maximizingPlayer = Marks.nought
        self.gameBoard = GameBoard(3)
        self.gameBoard.set_mark(0, Marks.empty)
        self.gameBoard.set_mark(1, Marks.cross)
        self.gameBoard.set_mark(2, Marks.nought)
        self.gameBoard.set_mark(3, Marks.empty)
        self.gameBoard.set_mark(4, Marks.cross)
        self.gameBoard.set_mark(5, Marks.cross)
        self.gameBoard.set_mark(6, Marks.nought)
        self.gameBoard.set_mark(7, Marks.nought)
        self.gameBoard.set_mark(8, Marks.cross)

        ultimateWinMove = self.computer.minimax(maximizingPlayer,
                                                self.gameBoard)
        self.assertEqual(ultimateWinMove, 1)

    def testMinimax_whenMinimizingPlayerUltimateWhin(self):
        maximizingPlayer = Marks.cross
        self.gameBoard = GameBoard(3)
        self.gameBoard.set_mark(0, Marks.empty)
        self.gameBoard.set_mark(1, Marks.nought)
        self.gameBoard.set_mark(2, Marks.cross)
        self.gameBoard.set_mark(3, Marks.empty)
        self.gameBoard.set_mark(4, Marks.nought)
        self.gameBoard.set_mark(5, Marks.nought)
        self.gameBoard.set_mark(6, Marks.cross)
        self.gameBoard.set_mark(7, Marks.cross)
        self.gameBoard.set_mark(8, Marks.nought)

        ultimateLoseMove = self.computer.minimax(maximizingPlayer,
                                                 self.gameBoard)
        self.assertEqual(ultimateLoseMove, -1)

    def testGetMove_whenItCanWin(self):
        maximizingPlayer = Marks.cross
        self.gameBoard = GameBoard(3)
        self.gameBoard.set_mark(0, Marks.cross)
        self.gameBoard.set_mark(1, Marks.cross)

        winMove = self.computer.get_move(self.gameBoard)
        self.assertEqual(winMove, 2)

    def testGetMove_whenItShouldBlockTheAdversaire(self):
        maximizingPlayer = Marks.cross
        self.gameBoard = GameBoard(3)
        self.gameBoard.set_mark(0, Marks.nought)
        self.gameBoard.set_mark(1, Marks.nought)

        blockOpposantWinMove = self.computer.get_move(self.gameBoard)
        self.assertEqual(blockOpposantWinMove, 2)

    def testGetMove_whenCanHaveAnUltimateWin(self):
        maximizingPlayer = Marks.cross
        self.gameBoard = GameBoard(3)
        self.gameBoard.set_mark(0, Marks.cross)
        self.gameBoard.set_mark(1, Marks.nought)
        self.gameBoard.set_mark(2, Marks.empty)
        self.gameBoard.set_mark(3, Marks.cross)
        self.gameBoard.set_mark(4, Marks.empty)
        self.gameBoard.set_mark(5, Marks.empty)
        self.gameBoard.set_mark(6, Marks.nought)
        self.gameBoard.set_mark(7, Marks.empty)
        self.gameBoard.set_mark(8, Marks.empty)

        ultimateWinMove = self.computer.get_move(self.gameBoard)
        self.assertEqual(ultimateWinMove, 4)

if __name__ == '__main__':
    unittest.main()
