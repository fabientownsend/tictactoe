import unittest

from fake_console_ui import FakeConsoleUI
from game_board import GameBoard
from human import Human
from marks_enum import Marks


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
        self.fakeConsoleUI.player_move_position = 5
        self.human = Human(Marks.nought, self.fakeConsoleUI)
        self.gameBoard = GameBoard(3)

        humanPlayerMove = self.human.get_move(self.gameBoard)

        self.assertEqual(humanPlayerMove, 5)

    def testGetMove_whenGetMoveTooLow(self):
        self.fakeConsoleUI.player_move_position = -10
        self.human = Human(Marks.nought, self.fakeConsoleUI)
        self.gameBoard = GameBoard(3)

        self.human.get_move(self.gameBoard)

        self.assertTrue(self.fakeConsoleUI.passed_in_wrong_range)

    def testGetMove_whenItsAnUsedSpot(self):
        self.fakeConsoleUI.player_move_position = 1
        self.human = Human(Marks.nought, self.fakeConsoleUI)
        self.gameBoard = GameBoard(3)
        self.gameBoard.set_mark(1, Marks.cross)

        self.human.get_move(self.gameBoard)

        self.assertTrue(self.fakeConsoleUI.passed_in_spot_not_free)

if __name__ == '__main__':
    unittest.main()
