import unittest
from stats import stdPy

class stdTest(unittest.TestCase):

    def meanTest(self):
        self.assertTrue(stdPy().mean(),57)

    def varianceTest(self):
        self.assertTrue(stdPy().variance(),740)

    def stdTest(self):
        self.assertTrue(stdPy().standardDeviation(),27)

if __name__ == '__main__':
    unittest.main()