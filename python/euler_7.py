# What is the 10001st prime number?
from math import sqrt

primes = [2]


def is_prime(n):
    for i in range(3, int(sqrt(n)) + 1):
        if not n % i:
            return False
    else:
        return True

j = 1
while len(primes) != 10001:
    j += 2
    if is_prime(j):
        primes.append(j)


print(primes[-1])

