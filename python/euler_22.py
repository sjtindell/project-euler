alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
names = list()
name_scores_total = 0

with open("euler_22.txt", "r") as f:
  names = [name.strip('"') for line in f for name in line.split(",")]

names = sorted(names)
for name in names:
  alphabet_value = 0
  for char in name:
    i = alphabet.index(char) + 1
    alphabet_value += i
  location = names.index(name) + 1
  total = alphabet_value * location
  name_scores_total += total

print(name_scores_total)
