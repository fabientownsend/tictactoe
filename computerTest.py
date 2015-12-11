import unittest
from computer import Computer
from marksEnum import Marks

class ComputerTest(unittest.TestCase):
    def setUp(self):
        self.computer = Computer()

    """
    def testBestMove(self):
        board  = [
            Marks.empty, Marks.cross, Marks.cross,
            Marks.empty, Marks.empty, Marks.empty,
            Marks.empty, Marks.empty, Marks.empty
        ]
        response = self.computer.bestMove(board)
        self.assertEqual(response, 0)
"""

    def testBestMove2(self):
        board  = [
            Marks.nought, Marks.nought, Marks.empty,
            Marks.cross, Marks.empty, Marks.cross,
            Marks.empty, Marks.empty, Marks.empty
        ]
        response = self.computer.bestMove(board)
        self.assertEqual(response, 4)

if __name__ == '__main__':
    unittest.main()
