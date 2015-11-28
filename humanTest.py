import unittest
from marksEnum import Marks
from human import Human

class TestHuman(unittest.TestCase):
    def setUp(self):
        self.player = Human()

    def testSetMark_whenMarkIsX(self):
        self.player.setMark(Marks.cross)
        self.assertEqual(self.player.mark, Marks.cross)

    def testSetMark_whenMarkIsO(self):
        self.player.setMark(Marks.round)
        self.assertEqual(self.player.mark, Marks.round)

if __name__ == '__main__':
    unittest.main()
