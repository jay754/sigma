import unittest
from stats import stdPy

class stdTest(unittest.TestCase):

    def meanTest(self):
        self.assertEqual(stdPy.mean(), 57)

    def varianceTest(self):
        self.assertEqual(stdPy.variance(), 740)

    def stdTest(self):
        self.assertEqual(stdPy.standardDeviation(), 27)

if __name__ == '__main__':
    unittest.main()