# Find the maximum sum total from the top to the bottom
# of the triangle below

with open("euler_18.txt", "r") as f:
  f = [ [int(chars) for chars in line.strip().split()] for line in f ]
  f = list(reversed(f))
  for x, line in enumerate(f):
    for y, num in enumerate(line):
      try:
        next_num = line[y + 1]
        if num >= next_num:
          f[x + 1][y] += num
        else:
          f[x + 1][y] += next_num
      except IndexError:
        pass
