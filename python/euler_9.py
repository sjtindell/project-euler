# There exists one pythagorean triplet for which a + b + c = 1000
# Find the product abc.

for x in range(1, 500):
    for y in range(1, 500):
        for z in range(1, 500):
            if x ** 2 + y ** 2 == z ** 2 and x + y + z == 1000:
                print(x * y * z)