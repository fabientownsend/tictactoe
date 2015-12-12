import unittest
from computer import Computer
from marksEnum import Marks

class ComputerTest(unittest.TestCase):
    def setUp(self):
        self.computer = Computer(1)

    def testInitialisation(self):
        self.assertEqual(self.computer.idPlayer, 1)

if __name__ == '__main__':
    unittest.main()
