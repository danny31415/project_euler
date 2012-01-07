"""Project Euler Problem 5

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.  What is the smallest positive
number that is evenly divisible by all of the numbers from 1 to 20?

"""
from __future__ import print_function

# the product of all primes from 1 to 20 should work
import prime

def main():
    return reduce(prime.lcm, range(2,20))

if __name__ == "__main__":
    main(argv)
