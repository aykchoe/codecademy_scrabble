def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter.upper(), 0)
  return point_total
  
def update_points_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
      player_to_points[player] = player_points
    print(player + ": " + str(player_points))
  print("\n")
  
def play_word(player, word):
  try:
    player_to_words.get(player).append(word)
    print(player + " played " + word + ".")
    print(word + " is worth " + str(score_word(word)) + "\n")
    update_points_totals()
    #print(player_to_points)
  except:
    print("Player: " + player + " does not exist. Cannot play word.")

def check_players():
    while True:
        num_of_players = int(input("How many players in this game?"))
        if num_of_players > 1 and num_of_players < 5:
            break
        print("Number of players must be between 2 and 4. Please enter a valid number of players.")
    return num_of_players
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letter_to_points = {key:value for key,value in zip(letters,points)}
letter_to_points[" "] = 0
player_to_points = {}
players = []

#Game
#Press enter to start the game
input("Press 'Enter' to start the game.")

#How many players?
num_of_players = check_players()

#Enter player names
for x in range(num_of_players):
    players.append(input("Player " + str(x + 1)))
player_to_words = {}
player_to_words = {player:[] for player in players}
player_turn = 0
print("\n")
for player in player_to_words:
    print(player + ": " + str(0))
while True:
    current_player = players[player_turn]
    played_word = input(current_player + "'s turn. Enter a word to play.")
    play_word(current_player, played_word)
    if player_to_points[current_player] > 100:
        print(current_player + " has won!")
        break
    #move to next player
    if player_turn == num_of_players-1:
        player_turn = 0
    else:
        player_turn +=1
