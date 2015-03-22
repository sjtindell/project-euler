# What is the smallest positive number evenly divisible by all the numbers from 1 to 20?

i = 1
found = False
while not found:
    i += 1
    print(i)
    for x in range(1, 21):
        if i % x:
            break
        elif not i % x and x == 19:
            print(i)
            found = True