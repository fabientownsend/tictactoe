import unittest

from fakeConsoleUI import FakeConsoleUI
from gameBoard import GameBoard
from human import Human
from marksEnum import Marks


class TestHuman(unittest.TestCase):
    def setUp(self):
        self.fakeConsoleUI = FakeConsoleUI()

    def testSetMark_whenMarkIsCrossself(self):
        self.human = Human(Marks.cross, self.fakeConsoleUI)
        self.assertEqual(self.human.mark, Marks.cross)

    def testSetMark_whenMarkIsNought(self):
        self.human = Human(Marks.nought, self.fakeConsoleUI)
        self.assertEqual(self.human.mark, Marks.nought)

    def testGetMove_whenCorrectValue(self):
        self.fakeConsoleUI.playerMovePosition = 5
        self.human = Human(Marks.nought, self.fakeConsoleUI)
        self.gameBoard = GameBoard(3)

        humanPlayerMove = self.human.getMove(self.gameBoard)

        self.assertEqual(humanPlayerMove, 5)

    def testGetMove_whenGetMoveTooLow(self):
        self.fakeConsoleUI.playerMovePosition = -10
        self.human = Human(Marks.nought, self.fakeConsoleUI)
        self.gameBoard = GameBoard(3)

        self.human.getMove(self.gameBoard)

        self.assertTrue(self.fakeConsoleUI.passedDisplayRangeBoardMethod)

    def testGetMove_whenItsAnUsedSpot(self):
        self.fakeConsoleUI.playerMovePosition = 1
        self.human = Human(Marks.nought, self.fakeConsoleUI)
        self.gameBoard = GameBoard(3)
        self.gameBoard.setMark(1, Marks.cross)

        self.human.getMove(self.gameBoard)

        self.assertTrue(self.fakeConsoleUI.passedInSpotNotFreeMethod)

if __name__ == '__main__':
    unittest.main()
