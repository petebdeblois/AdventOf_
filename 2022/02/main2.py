file = open('test.txt')

games = file.read().strip().split('\n')

action = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}

scores_my_hand = {
    'A': 1,
    'B': 2,
    'C': 3,
}
scores = 0

all_games = []
for i in range(len(games)):
  new = games[i].split(' ')
  all_games.append(new)

for game in range(len(all_games)):
  if all_games[game][0] == 'A':
    if all_games[game][1] == 'X':
      scores += scores_my_hand['B']
      scores += action[all_games[game][1]]
    elif all_games[game][1] == 'Y':
      scores += scores_my_hand[all_games[game][0]]
      scores += action[all_games[game][1]]
    else:
      scores += action[all_games[game][1]]

  if all_games[game][0] == 'B':
    if all_games[game][1] == 'X':
      scores += scores_my_hand['A']
      scores += action[all_games[game][1]]
    elif all_games[game][1] == 'Y':
      scores += scores_my_hand[all_games[game][0]]
      scores += action[all_games[game][1]]
    else:
      scores += action[all_games[game][1]]

  if all_games[game][0] == 'C':
    if all_games[game][1] == 'X':
      scores += scores_my_hand['B']
      scores += action[all_games[game][1]]
    if all_games[game][1] == 'Y':
      scores += scores_my_hand[all_games[game][0]]
      scores += action[all_games[game][1]]
    else:
      scores += scores_my_hand['A']
      scores += action[all_games[game][1]]
  print(scores)


print(scores)

