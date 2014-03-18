"""

Simple Python standard Deviation, variance, and mean calculator

Tested using randomly generated data

"""

from random import randint
import os
import math

def randomNumbers():

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

# else:
# 	print data

def mean():
	return (sum(randomNumbers())/len(randomNumbers()))

def variance():
	return sum(map(lambda x: x ** 2, [i-mean() for i in randomNumbers()]))/len(randomNumbers())

def standardDeviation():
	return math.sqrt(variance())

def main():
	print mean() #57
	print variance() #725
	print standardDeviation() #26.9258240357

main()
