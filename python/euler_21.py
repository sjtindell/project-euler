def div_sum(n):
  return sum(div for div in range(1, n) if n % div == 0)

amicables = set()

for x in range(1, 10000):
  a = div_sum(x)
  for y in range(1, 10000):
    if y == a:
      b = div_sum(y)
      if b == x and x != y:
        amicables.add(x)
        amicables.add(y)

print(sum(amicables))
