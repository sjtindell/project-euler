# Start in the top left of a 20 x 20 grid. Moving right and down, how many
# routes are there to the bottom right corner?


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# 20 by 20 grid
all_moves = factorial(40)
down_moves = right_moves = factorial(20)

paths = all_moves / (down_moves * right_moves)

print(paths)







