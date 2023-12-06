import numpy as np

file = open('input.txt')

rucksacks = file.read().strip().split('\n')
output = []
numbers = []
chunk_size = 3

amount =  int(len(rucksacks)/3)
groups = np.array_split(rucksacks, amount)


for i in range(len(groups)):
  for y in range(len(groups[i][0])):
    if groups[i][0][y] in groups[i][1]:
      if groups[i][0][y] in groups[i][2]:
        output.append(groups[i][0][y])
        break

for letter in output:
  if letter.islower():
    number = ord(letter) - 96
  else:
    number = ord(letter) - 64
    number += 26
  numbers.append(number)

print(sum(numbers))
