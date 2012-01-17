"""Project Euler Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

"""
from __future__ import print_function
import prime
import numpy

def nth_prime(n):
    count = 0
    for the_prime in prime.gen_primes():
        count += 1
        if count == n:
            return the_prime

def main():
    return nth_prime(10001)

if __name__ == "__main__":
    print(main())
