# Which starting number under 1000000 produces the longest collatz chain?


def collatz(start):
    chain = [start]
    while start != 1:
        if not start % 2:
            start /= 2
        else:
            start = 3 * start + 1
        chain.append(int(start))
    return len(chain)

longest_chain = 0
answer = 0

for x in range(1, 1000000):
    test = collatz(x)
    if test > longest_chain:
        longest_chain = test
        answer = x

print(answer)

