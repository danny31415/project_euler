def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

primes = [2,3,5,7,11]

def is_prime(num):
    if num in primes:
        return True
    for p in primes:
        if num % p == 0:
            return False
    primes.append(num)
    return True

def gen_primes_in_range(min, max):
    for num in range(min, max):
        if is_prime(num):
            yield num

def factors(n):
    # return a list of prime factors
    limit = n**0.5  
    i = 2
    while i <= limit:
        if n % i == 0:
            yield i
            n /= i
            limit = n**0.5
        else:
            i += 1
    if n > 1:
        yield n
