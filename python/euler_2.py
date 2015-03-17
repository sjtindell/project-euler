# By considering the terms in the Fibonacci sequence
# whose values do not exceed four million, find the
# sum of the even-valued terms.
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...


def fibonacci(stop):
    a, b = 0, 1
    nums = []

    while b < stop:
        a, b = b, a + b

        if b % 2 == 0:
            nums.append(b)

    return sum(nums)
