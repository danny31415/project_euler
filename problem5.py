# Problem 5
# 30 November 2001

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# the product of all primes from 1 to 20 should work
import prime

print(reduce(prime.lcm, range(2,20)))
