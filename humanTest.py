import unittest

from fakeConsoleUI import FakeConsoleUI
from human import Human
from marksEnum import Marks


class TestHuman(unittest.TestCase):
    def setUp(self):
        self.fakeConsoleUI = FakeConsoleUI()

    def testSetMark_whenMarkIsCrossself(self):
        self.player = Human(Marks.cross, self.fakeConsoleUI)
        self.assertEqual(self.player.mark, Marks.cross)

    def testSetMark_whenMarkIsNought(self):
        self.player = Human(Marks.nought, self.fakeConsoleUI)
        self.assertEqual(self.player.mark, Marks.nought)

    def testGetMove_whenCorrectValue(self):
        self.fakeConsoleUI.move = 4
        self.player = Human(Marks.nought, self.fakeConsoleUI)
        board = [
            Marks.empty, Marks.empty, Marks.empty,
            Marks.empty, Marks.empty, Marks.empty,
            Marks.empty, Marks.empty, Marks.empty
        ]
        result = self.player.getMove(board)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()
