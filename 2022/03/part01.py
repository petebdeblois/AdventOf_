file = open('input.txt')

rucksacks = file.read().strip().split('\n')
output = []

def compare(a, b):
    for x in range(len(a)):
      for y in range(len(b)):
        if a[x] == b[y]:
          return a[x]

for list in rucksacks:
  first_half = list[:len(list)//2]
  second_half = list[len(list)//2:]
  letter = compare(first_half, second_half)
  if letter.islower():
    number = ord(letter) - 96
  else:
    number = ord(letter) - 64
    number += 26
  output.append(number)

print(sum(output))
