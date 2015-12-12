import unittest
from computer import Computer
from marksEnum import Marks

class ComputerTest(unittest.TestCase):
    def setUp(self):
        self.computer = Computer(1)
        self.computer.mark = Marks.cross

    def testInitialisation(self):
        self.assertEqual(self.computer.idPlayer, 1)

    def testSwtich_whenMarkIsCross(self):
        response = self.computer.switch(Marks.cross)
        self.assertEqual(response, Marks.nought)

    def testSwtich_whenMarkIsNought(self):
        response = self.computer.switch(Marks.nought)
        self.assertEqual(response, Marks.cross)

    def testMinimax_whenMaximizingPlayerWin(self):
        maximizingPlayer = Marks.cross
        board  = [
            Marks.cross, Marks.cross, Marks.cross,
            Marks.empty, Marks.empty, Marks.empty,
            Marks.empty, Marks.empty, Marks.empty
        ]

        response = self.computer.minimax(maximizingPlayer, board)
        self.assertEqual(response, 1)

    def testMinimax_whenMinimizinglayerWin(self):
        maximizingPlayer = Marks.cross
        board  = [
            Marks.nought, Marks.nought, Marks.nought,
            Marks.empty, Marks.empty, Marks.empty,
            Marks.empty, Marks.empty, Marks.empty
        ]

        response = self.computer.minimax(maximizingPlayer, board)
        self.assertEqual(response, -1)

    def testMinimax_whenItsDraw(self):
        maximizingPlayer = Marks.cross
        board  = [
            Marks.nought, Marks.cross, Marks.nought,
            Marks.nought, Marks.cross, Marks.cross,
            Marks.cross, Marks.nought, Marks.cross
        ]

        response = self.computer.minimax(maximizingPlayer, board)
        self.assertEqual(response, 0)

    def testMinimax_whenMaximizingUltimateWhin(self):
        maximizingPlayer = Marks.nought
        board  = [
            Marks.empty, Marks.cross, Marks.nought,
            Marks.empty, Marks.cross, Marks.cross,
            Marks.nought, Marks.nought, Marks.cross
        ]

        response = self.computer.minimax(maximizingPlayer, board)
        self.assertEqual(response, 1)

    def testMinimax_whenMinimizingUltimateWhin(self):
        maximizingPlayer = Marks.cross
        board  = [
            Marks.empty, Marks.nought, Marks.cross,
            Marks.empty, Marks.nought, Marks.nought,
            Marks.cross, Marks.cross, Marks.nought
        ]

        response = self.computer.minimax(maximizingPlayer, board)
        self.assertEqual(response, -1)

if __name__ == '__main__':
    unittest.main()
