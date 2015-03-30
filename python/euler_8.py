# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
# What is the value of this product?


main_list = []
greatest_product = 0


def product(num_list):
    prod = 1
    for num in num_list:
        prod *= num
    return prod

with open('euler_8.txt', 'r') as f:
    for line in f:
        line = list(int(char) for char in line.strip())
        main_list += line

a, b = 0, 13
while a < len(main_list):
    nums = main_list[a:b]
    if product(nums) > greatest_product:
        greatest_product = product(nums)
    a += 1
    b += 1

print(greatest_product)