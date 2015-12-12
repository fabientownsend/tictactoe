import unittest
from marksEnum import Marks
from gamePolicy import GamePolicy

class GamePolicyTest(unittest.TestCase):
    def setUp(self):
        self.gamePolicy = GamePolicy()

    def testCheckTie_whenItsTie(self):
        maximizingPlayer = Marks.cross
        board  = [
            Marks.cross, Marks.cross, Marks.cross,
            Marks.cross, Marks.cross, Marks.cross,
            Marks.cross, Marks.cross, Marks.cross
        ]

        response = self.gamePolicy.checkTie(board)
        self.assertEqual(response, True)

    def testCheckTie_whenItsNotTie(self):
        maximizingPlayer = Marks.cross
        board  = [
            Marks.cross, Marks.cross, Marks.cross,
            Marks.cross, Marks.empty, Marks.cross,
            Marks.cross, Marks.cross, Marks.cross
        ]

        response = self.gamePolicy.checkTie(board)
        self.assertEqual(response, False)

    def testWin_whenLineOneWin(self):
        board  = [
            Marks.cross, Marks.cross, Marks.cross,
            Marks.empty, Marks.empty, Marks.empty,
            Marks.empty, Marks.empty, Marks.empty
        ]
        response = self.gamePolicy.win(Marks.cross, board)
        self.assertEqual(response, True)

    def testWin_whenLineTwoWin(self):
        board  = [
            Marks.empty, Marks.empty, Marks.empty,
            Marks.cross, Marks.cross, Marks.cross,
            Marks.empty, Marks.empty, Marks.empty
        ]
        response = self.gamePolicy.win(Marks.cross, board)
        self.assertEqual(response, True)

    def testWin_whenLineThreeWin(self):
        board  = [
            Marks.empty, Marks.empty, Marks.empty,
            Marks.empty, Marks.empty, Marks.empty,
            Marks.cross, Marks.cross, Marks.cross,
        ]
        response = self.gamePolicy.win(Marks.cross, board)
        self.assertEqual(response, True)

    def testWin_whenColumnsOneWin(self):
        board  = [
            Marks.cross, Marks.empty, Marks.empty,
            Marks.cross, Marks.empty, Marks.empty,
            Marks.cross, Marks.empty, Marks.empty,
        ]
        response = self.gamePolicy.win(Marks.cross, board)
        self.assertEqual(response, True)

    def testWin_whenColumnsTwoWin(self):
        board  = [
            Marks.empty, Marks.cross, Marks.empty,
            Marks.empty, Marks.cross, Marks.empty,
            Marks.empty, Marks.cross, Marks.empty,
        ]
        response = self.gamePolicy.win(Marks.cross, board)
        self.assertEqual(response, True)

    def testWin_whenColumnsThreeWin(self):
        board  = [
            Marks.empty, Marks.empty, Marks.cross,
            Marks.empty, Marks.empty, Marks.cross,
            Marks.empty, Marks.empty, Marks.cross,
        ]
        response = self.gamePolicy.win(Marks.cross, board)
        self.assertEqual(response, True)

    def testWin_whenDialOneWin(self):
        board  = [
            Marks.cross, Marks.empty, Marks.empty,
            Marks.empty, Marks.cross, Marks.empty,
            Marks.empty, Marks.empty, Marks.cross,
        ]
        response = self.gamePolicy.win(Marks.cross, board)
        self.assertEqual(response, True)

    def testWin_whenDialTwoWin(self):
        board  = [
            Marks.empty, Marks.empty, Marks.cross,
            Marks.empty, Marks.cross, Marks.empty,
            Marks.cross, Marks.empty, Marks.empty,
        ]
        response = self.gamePolicy.win(Marks.cross, board)
        self.assertEqual(response, True)

if __name__ == '__main__':
    unittest.main()
