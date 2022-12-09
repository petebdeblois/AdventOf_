file = open('input.txt')

bag = file.read().split('\n')

def main():
  currentCalories = 0
  totals = []
  for cookies in bag:
    if (not cookies):
      totals.append(currentCalories)
      currentCalories = 0
    else:
      currentCalories += int(cookies)
  totals.append(currentCalories)
  # findMaxes(totals)
  return totals



def findMax(totals):
  # initiate the max as the first element
  max = totals[0]
  for i in range(0, len(totals)):
      # Compare elements of array with max
    if (totals[i] > max):
        max = totals[i]
  # print(totals.index(max) +1)
  return max

def findMaxes(totals):
  totals.sort(reverse=True)
  total_top_3 = 0
  for i in range(3):
    total_top_3 += int(totals[i])
  return total_top_3 


if __name__ == '__main__':
  totals = main()
  print(f'Here is the top elve number of cal {findMax(totals)}')
  print(f'Here is the top 3 elves number of cal {findMaxes(totals)}')
