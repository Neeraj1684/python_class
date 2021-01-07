cricket_players = {}
cricket_players["ajinkya"] = 1
cricket_players["virat"] = 7
cricket_players["jadeja"] = 3
cricket_players["bumrah"] = 5
cricket_players["bhuvneshwar"] = 2

for player_name in cricket_players:
  print(player_name)

for player_name in cricket_players.values():
  print(player_name)

for player_name,player_val in cricket_players.items():
  print(player_name+" " + str(player_val))

def checkKey(cricket_players, key):
  if key in cricket_players:
    print("found")
  else:
    print("not found")

key = 'virat'
checkKey(cricket_players, key)
   
output

#ajinkya
#virat
#jadeja
#bumrah
#bhuvneshwar
#1
#7
#3
#5
#2
#ajinkya 1
#virat 7
#jadeja 3
#bumrah 5
#bhuvneshwar 2
#found
