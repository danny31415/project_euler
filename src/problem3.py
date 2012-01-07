"""Project Euler Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.  What is the largest
prime factor of the number 600851475143 ?

"""
from __future__ import print_function

primes = [2,3,5,7,11]

def is_prime(num):
    if num in primes:
        return True
    for p in primes:
        if num % p == 0:
            return False
    primes.append(num)
    return True

def main():
    # try to see if any of our primes are factors for the number
    # find another prime
    factors = []
    num = 600851475143
    next_try = 2
    
    while num > 1:
        while not(is_prime(next_try)):
            next_try += 1
        while num % next_try == 0:
            num = int(num/next_try)
            factors.append(next_try)
        next_try += 1
    return factors[-1]

if __name__ == "__main__":
    print(main())
