import decimal
context = decimal.Context(prec=1000)
decimal.setcontext(context)


def all_same(string):
  for c in string[1:]:
    if c != string[0]: 
      return False
  return True

def find_cycle(string):
  # slice by 2, slice by 3, etc...
  for x in range(2, int(len(string) / 2) + 1):
    pass

for i in range(2, 1000):
  dec = decimal.Decimal(1 / i)
  recip = str(dec)[2:]

  if len(recip) < 6 or all_same(recip):
    continue

  print(i, recip)
  cycle = find_cycle(recip)

# problem: we probably can't produce enough digits to 
# just check the string and find the largest cycle
