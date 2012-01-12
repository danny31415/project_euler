"""Project Euler Problem 6

The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""
from __future__ import print_function
import unittest

# both of these functions could be implemented without loops, but I'll put the O(n) version for now, because it should be quick anyway
def sum_of_squares(n):
    sum = 0
    for i in range (1, n+1):
        sum += i**2
    return sum

def square_of_sum(n):
    sum = 0
    for i in range (1, n+1):
        sum += i
    return sum ** 2

def main():
    return square_of_sum(100) - sum_of_squares(100)

if __name__ == "__main__":
    print(main())
