file = open('input.txt')

games = file.read().strip().split('\n')

scores_my_hand = {
  'X':1,
  'Y':2,
  'Z':3,
}
scores = 0

all_games = [] 
for i in range(len(games)):
  new = games[i].split(' ')
  all_games.append(new)

for game in range(len(all_games)):
  scores += scores_my_hand[str(all_games[game][1])]
  if all_games[game][0] == 'A':
    if all_games[game][1] == 'Y':
      scores += 6
    elif all_games[game][1] == 'X':
      scores += 3
    else:
      scores += 0
  elif all_games[game][0] == 'B':
    if all_games[game][1] == 'Z':
      scores += 6
    elif all_games[game][1] == 'Y':
      scores += 3
    else:
      scores += 0
  else:
    if all_games[game][1] == 'X':
      scores += 6
    elif all_games[game][1] == 'Z':
      scores += 3
    else:
      scores += 0
  print(f'scores: {scores} games: {game}')



print(scores)
