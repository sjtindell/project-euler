def all_same(string):
  for c in string[1:]:
    if c != string[0]: 
      return False
  return True


for i in range(2, 11):
  dec = 1 / i
  recip = str(dec)[2:]
  
  if len(recip) < 6 or all_same(recip):
    continue

  print(recip) 
