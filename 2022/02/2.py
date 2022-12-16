file = open('input.txt')

games = file.read().strip().split('\n')

combo = {
  'A X': 3,
  'A Y': 4,
  'A Z': 8,
  'B X': 1,
  'B Y': 5,
  'B Z': 9,
  'C X': 2,
  'C Y': 6,
  'C Z': 7
}
scores = 0

for game in range(len(games)):
  if games[game] in combo:
    scores += combo[games[game]]

print(scores)
