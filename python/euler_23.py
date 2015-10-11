def is_abundant(n):
  x = 0
  for y in range(1, n):
    if n % y == 0:
      x += y
  if x > n: 
    return True
  return False

abundants = []
abundant_sums = []
answer = 0

for x in range(28123):
  if is_abundant(x):
    abundants.append(x)
    for num in abundants:
      abundant_sums.append(x + num)

print("starting...") 
for j in range(28123):
  if j not in abundant_sums:
    answer += j
  print(j)

print(answer)


