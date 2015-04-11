# What is the value of the first triangle number to have over 500 divisors?


def triangles():
    j, k = 0, 0
    while True:
        j += 1
        k += j
        yield k

for triangle in triangles():

    factors = []

    for i in range(1000000, int(triangle / 2) + 1):
        if not triangle % i:
            factors.append(i)
    if len(factors) > 500:
        break
