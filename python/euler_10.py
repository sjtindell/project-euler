# sum all primes below 2 million

from math import sqrt


def is_prime(n):

    for i in range(int(sqrt(n)) + 1):
        if i in (0, 1):
            pass
        elif not n % i:
            return False
    else:
        return True


answer = sum(num for num in range(2, 2000000) if is_prime(num))
print(answer)
