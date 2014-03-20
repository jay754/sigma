"""

Simple Python standard Deviation, variance, and mean calculator

Tested using randomly generated data

Using the The Sample Standard Deviation (still not much difference in the standard deviation if the sample size if big)

"""

from random import randint
import os
import math

class stdPy(object):

    def __init__(self):

        size = os.stat('numbers.txt').st_size #size of the file to make sure that it isn't filled already

        if size == 0:
            data = [randint(0,100) for i in range(50)]
            filewriteOBJ = open('numbers.txt', 'w')
            for i in data:
                fileOBJ.write(str(i)+'\n')
        else:
            filereadOBJ = open('numbers.txt', 'r')
            self.data = [int(i) for i in filereadOBJ]

    def mean(self):
        """
        returns the mean/average of the sample data
        """

        return (sum(self.data))/(len(self.data))

    def variance(self):
        """
        returns the variance of the sample data
        """

        return sum(map(lambda x: x ** 2, [i-self.mean() for i in self.data]))/(len(self.data)-1)

    def standardDeviation(self):
        """
        Returns standard deviation of the sample data
        """

        return round(math.sqrt(self.variance()))

    def withinSTD(self):
        """
        Returns the percent of numbers that are not part of the standard deviation
        """

        upperBound = self.mean() + self.standardDeviation()
        lowerBound = self.mean() - self.standardDeviation()

        numsNotInSTD = []

        for i in self.randomNumbers():
            if i > upperBound or i < lowerBound:
                numsNotInSTD.append(i)

        return float(len(numsNotInSTD))/float(len(self.data))*100