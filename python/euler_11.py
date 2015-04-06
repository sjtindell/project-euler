# What is the greatest product of four adjacent numbers in the 20 x 20 grid?


def product(nums):
    p = 1
    for n in nums:
        p *= n
    return p

grid = []

with open('euler_11.txt', 'r+') as f:
    for line in f:
        grid += list(int(char) for char in line.strip().split())

answer = 0
i = 0

for _ in grid:

    sub_lists = [
        # right
        grid[i: i + 4],
        #left
        grid[i - 3:i + 1],
        # up
        grid[i:i - 80:-20],
        # down
        grid[i:i + 80:20],
        # left diagonal up
        grid[i:i - 64:-21],
        # right diagonal up
        grid[i:i - 58:-19],
        # left diagonal down
        grid[i:i + 64:21],
        # right diagonal down
        grid[i:i + 58:19]
    ]

    for sub_list in sub_lists:
        try:
            prod = product(sub_list)
            if prod > answer:
                answer = prod
        except IndexError:
            pass
    i += 1

print(answer)













# check 3 + 1 back
# check 3 + 1 forward
