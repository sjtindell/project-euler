# Find the difference between the sum of the squares of
# the first one hundred natural nums and the square of the sum.


sum_squares = sum(x ** 2 for x in range(1, 101))
square_sum = sum(x for x in range(1, 101)) ** 2

difference = square_sum - sum_squares

print(difference)
