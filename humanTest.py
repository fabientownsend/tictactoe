import unittest
from marksEnum import Marks
from human import Human

class TestHuman(unittest.TestCase):
    def setUp(self):
        self.player = Human(1)

    def testInitialisation(self):
        self.assertEqual(self.player.idPlayer, 1)

    def testSetMark_whenMarkIsCrossself(self):
        self.player.setMark(Marks.cross)
        self.assertEqual(self.player.mark, Marks.cross)

    def testSetMark_whenMarkIsNought(self):
        self.player.setMark(Marks.nought)
        self.assertEqual(self.player.mark, Marks.nought)

if __name__ == '__main__':
    unittest.main()
