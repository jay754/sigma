"""

Simple Python standard Deviation, variance, and mean calculator

Tested using randomly generated data

"""

from random import randint
import os
import math

def randomNumbers():

    """

    randomly generated data

    """

    size = os.stat('numbers.txt').st_size #size of the file to make sure that it isn't filled already

    if size == 0:
        data = [randint(0,100) for i in range(50)]
        filewriteOBJ = open('numbers.txt', 'w')
        for i in data:
            fileOBJ.write(str(i)+'\n')
    else:
        filereadOBJ = open('numbers.txt', 'r')
        data = [int(i) for i in filereadOBJ]

    return data

def mean():

    """

    returns the mean/average of the sample data

    """


    return (sum(randomNumbers())/len(randomNumbers()))

def variance():
    """

    returns the variance of the sample data

    """

    return sum(map(lambda x: x ** 2, [i-mean() for i in randomNumbers()]))/len(randomNumbers())

def standardDeviation():
    """

    Returns standard deviation of the sample data

    """

    return round(math.sqrt(variance()))

def withinSTD():
    """

    Returns the percent of numbers that are not part of the standard deviation

    """

    upperBound = mean() + standardDeviation()
    lowerBound = mean() - standardDeviation()

    numsNotInSTD = []

    for i in randomNumbers():
        if i > upperBound or i < lowerBound:
            numsNotInSTD.append(i)

    return float(len(numsNotInSTD))/float(len(randomNumbers()))*100

def main():
    print mean() #57
    print variance() #725
    print standardDeviation() #26.9258240357
    print withinSTD() # 40.0

main()
