import unittest
from initialisationTravis import InitialisationTravis

class TestInitialisationTravis(unittest.TestCase):
    def setUp(self):
        self.travis = InitialisationTravis()

    def testFirstTest_whenItsASuccess(self):
        self.assertEqual(self.travis.firstTest(), "success")

if __name__ == '__main__':
    unittest.main()
