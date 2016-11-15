#Write a library that contains a class that can represent any 2𝑥2 real matrice. 
#Include two functions to calculate the sum and product of two matrices. 
#Next, write a program that imports this library module and use it to perform calculations.
#Examples:
#
# matrix_1 = Matrix(4,5,6,7)
# matrix_2 = Matrix(2,2,2,1)
#
# matrix_3 = matrix_2.add(matrix_1)
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#(If you want you can expand implementation to NxN matrix.)
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#When you are done upload this code to your github repository. 
#The whole repository MUST be named "kol_gr2"! 
#
#Delete these comments before commit!
#Good luck.

from Matrix import *

def main():

	matrix_1 = Matrix(4,5,6,7)
	matrix_2 = Matrix(2,2,2,1)

	matrix_3 = matrix_2.summ(matrix_1)
	matrix_4 = matrix_2.diff(matrix_1)
	matrix_5 = matrix_2.mult(matrix_1)

	print matrix_3
	print matrix_4
	print matrix_5

	matrix_6 = matrix_2 + matrix_1
	matrix_7 = matrix_2 + 5
	matrix_8 = 5 + matrix_2

	print matrix_6
	print matrix_7
	print matrix_8

	matrix_9 = matrix_2 - matrix_1
	matrix_10 = matrix_2 - 4

	print matrix_9
	print matrix_10

	matrix_11 = matrix_2 * matrix_1
	matrix_12 = matrix_2 * 3
	matrix_13 = 3 * matrix_2

	print matrix_11
	print matrix_12
	print matrix_13

	v = matrix_13.vector()
	print v.next()
	print v.next()
		

if __name__ == "__main__":
        main()

