import unittest
from minimax import Minimax
from marksEnum import Marks

class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.minimax = Minimax()

    def testCheckTie_whenItIsTie(self):
        board  = [
            Marks.cross, Marks.cross, Marks.cross,
            Marks.cross, Marks.cross, Marks.cross,
            Marks.cross, Marks.cross, Marks.cross
        ]
        response = self.minimax.checkTie(board)
        self.assertEqual(response, True)

    def testCheckTie_whenItIsNotTie(self):
        board  = [
            Marks.empty, Marks.cross, Marks.cross,
            Marks.cross, Marks.cross, Marks.cross,
            Marks.cross, Marks.cross, Marks.empty
        ]
        response = self.minimax.checkTie(board)
        self.assertEqual(response, False)

    def testMinimax_whenMaximizingPlayerWin(self):
        maximizingPlayer = Marks.cross
        board  = [
            Marks.cross, Marks.cross, Marks.cross,
            Marks.empty, Marks.empty, Marks.empty,
            Marks.empty, Marks.empty, Marks.empty
        ]

        response = self.minimax.minimax(maximizingPlayer, board)
        self.assertEqual(response, 1)

    def testMinimax_whenMinimizingPlayerWin(self):
        maximizingPlayer = Marks.nought
        board  = [
            Marks.nought, Marks.nought, Marks.nought,
            Marks.empty, Marks.empty, Marks.empty,
            Marks.empty, Marks.empty, Marks.empty
        ]

        response = self.minimax.minimax(maximizingPlayer, board)
        self.assertEqual(response, -1)

    def testMinimax_itsADrawn(self):
        maximizingPlayer = Marks.nought
        board  = [
            Marks.cross, Marks.nought, Marks.cross,
            Marks.nought, Marks.cross, Marks.nought,
            Marks.nought, Marks.cross, Marks.nought
        ]

        response = self.minimax.minimax(maximizingPlayer, board)
        self.assertEqual(response, 0)

if __name__ == '__main__':
    unittest.main()
