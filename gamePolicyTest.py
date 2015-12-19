import unittest

from gamePolicy import GamePolicy
from marksEnum import Marks


class GamePolicyTest(unittest.TestCase):
    def setUp(self):
        self.gamePolicy = GamePolicy()

    def testIsEmpty_whenItsEmpty(self):
        board  = [
            Marks.empty, Marks.empty, Marks.empty,
            Marks.empty, Marks.empty, Marks.empty,
            Marks.empty, Marks.empty, Marks.empty
        ]

        response = self.gamePolicy.isEmpty(board)
        self.assertTrue(response)

    def testIsEmpty_whenItsNotEmpty(self):
        board  = [
            Marks.empty, Marks.empty, Marks.empty,
            Marks.empty, Marks.cross, Marks.empty,
            Marks.empty, Marks.empty, Marks.empty
        ]

        response = self.gamePolicy.isEmpty(board)
        self.assertFalse(response)

    def testCheckTie_whenItsTie(self):
        maximizingPlayer = Marks.cross
        board  = [
            Marks.cross, Marks.nought, Marks.cross,
            Marks.nought, Marks.nought, Marks.cross,
            Marks.nought, Marks.cross, Marks.nought
        ]

        response = self.gamePolicy.checkTie(board)
        self.assertTrue(response)

    def testCheckTie_whenItsNotTieButWin(self):
        maximizingPlayer = Marks.cross
        board  = [
            Marks.cross, Marks.cross, Marks.cross,
            Marks.cross, Marks.empty, Marks.cross,
            Marks.cross, Marks.cross, Marks.cross
        ]

        response = self.gamePolicy.checkTie(board)
        self.assertFalse(response)

    def testWin_whenLineOneWin(self):
        board  = [
            Marks.cross, Marks.cross, Marks.cross,
            Marks.empty, Marks.empty, Marks.empty,
            Marks.empty, Marks.empty, Marks.empty
        ]
        response = self.gamePolicy.win(Marks.cross, board)
        self.assertTrue(response)

    def testWin_whenLineTwoWin(self):
        board  = [
            Marks.empty, Marks.empty, Marks.empty,
            Marks.cross, Marks.cross, Marks.cross,
            Marks.empty, Marks.empty, Marks.empty
        ]
        response = self.gamePolicy.win(Marks.cross, board)
        self.assertTrue(response)

    def testWin_whenLineThreeWin(self):
        board  = [
            Marks.empty, Marks.empty, Marks.empty,
            Marks.empty, Marks.empty, Marks.empty,
            Marks.cross, Marks.cross, Marks.cross,
        ]
        response = self.gamePolicy.win(Marks.cross, board)
        self.assertTrue(response)

    def testWin_whenColumnsOneWin(self):
        board  = [
            Marks.cross, Marks.empty, Marks.empty,
            Marks.cross, Marks.empty, Marks.empty,
            Marks.cross, Marks.empty, Marks.empty,
        ]
        response = self.gamePolicy.win(Marks.cross, board)
        self.assertTrue(response)

    def testWin_whenColumnsTwoWin(self):
        board  = [
            Marks.empty, Marks.cross, Marks.empty,
            Marks.empty, Marks.cross, Marks.empty,
            Marks.empty, Marks.cross, Marks.empty,
        ]
        response = self.gamePolicy.win(Marks.cross, board)
        self.assertTrue(response)

    def testWin_whenColumnsThreeWin(self):
        board  = [
            Marks.empty, Marks.empty, Marks.cross,
            Marks.empty, Marks.empty, Marks.cross,
            Marks.empty, Marks.empty, Marks.cross,
        ]
        response = self.gamePolicy.win(Marks.cross, board)
        self.assertTrue(response)

    def testWin_whenDialOneWin(self):
        board  = [
            Marks.cross, Marks.empty, Marks.empty,
            Marks.empty, Marks.cross, Marks.empty,
            Marks.empty, Marks.empty, Marks.cross,
        ]
        response = self.gamePolicy.win(Marks.cross, board)
        self.assertTrue(response)

    def testWin_whenDialTwoWin(self):
        board  = [
            Marks.empty, Marks.empty, Marks.cross,
            Marks.empty, Marks.cross, Marks.empty,
            Marks.cross, Marks.empty, Marks.empty,
        ]
        response = self.gamePolicy.win(Marks.cross, board)
        self.assertTrue(response)

    def testIsFree_whenItsFree(self):
        board  = [
            Marks.empty, Marks.empty, Marks.empty,
            Marks.empty, Marks.empty, Marks.empty,
            Marks.empty, Marks.empty, Marks.empty,
        ]
        response = self.gamePolicy.isFree(board, 0)
        self.assertTrue(response)

    def testIsFree_whenItsNotFree(self):
        board  = [
            Marks.cross, Marks.empty, Marks.empty,
            Marks.empty, Marks.empty, Marks.empty,
            Marks.empty, Marks.empty, Marks.empty,
        ]
        response = self.gamePolicy.isFree(board, 0)
        self.assertFalse(response)

if __name__ == '__main__':
    unittest.main()
