# What is the largest prime factor of the number 600851475143?

import math


def is_prime(n):

    for i in range(3, int(math.sqrt(n))):
        if i in (0, 1):
            pass
        elif not n % i:
            return False
    else:
        return True


def factor_factory(n):

    for i in range(3, int(math.sqrt(n) + 1), 2 if n % 2 else 1):
        if n % i == 0:
            yield i


def main(n):

    gpf = 0

    for num in factor_factory(n):
        if is_prime(num):
            gpf = num
        else:
            pass

    return gpf


print('gpf:', main(600851475143))

