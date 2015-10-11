def factorial(n):
  factorial_sum = 1
  for x in range(1, n + 1):
    factorial_sum *= x
  return factorial_sum

digit_str_list = list(str(factorial(100)))
digit_list = [int(char) for char in digit_str_list]
print(sum(digit_list))
