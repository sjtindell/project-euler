from itertools import permutations
from math import sqrt

answer = None
digits = []

def is_prime(n):
    for i in range(3, int(sqrt(n))):
        if i in (0, 1):
            pass
        elif not n % i:
            return False
    else:
        return True

for x in range(1, 10):
    digits.append(str(x))
    for perm in permutations(digits):
        string = ''.join(perm)
        if is_prime(int(string)):
            if int(perm[0]) != 0:
                answer = int(string)

print(answer)
