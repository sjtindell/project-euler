# Find the largest palindrome made from the product of two 3-digit numbers


def is_palindrome(num):
    string = str(num)
    if len(string) % 2 != 0:
        return False
    else:
        cutoff = int(len(string) / 2)
        head = string[:cutoff]
        tail = string[cutoff:]
        if head == tail[::-1]:
            return True
        else:
            return False


def gen_products(digits):
    limit = int(str(1) + str(0) * digits)
    for x in range(limit):
        for y in range(limit):
            yield x * y


def search():
    solution = 0
    for i in gen_products(3):
        if is_palindrome(i) and i > solution:
            solution = i
    return solution

