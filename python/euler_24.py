digit_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def permutate(elements):
  if len(elements) == 0:
    yield elements
  else:
    for perm in permutate(elements[1:]):
      for i, _ in enumerate(elements):
        yield perm[:i] + elements[0:1] + perm[i:]


tmp = [p for p in permutate(digit_list)]
permutations = sorted(tmp)

for index, entry in enumerate(permutations):
  if index == 999999:
    print(''.join(str(c) for c in entry))


