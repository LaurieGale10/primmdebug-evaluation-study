import random

player_input = 0
while player_input != 1 or player_input != 2:
	player_input = int(input("Player 1, enter your choice: 1 for rock, 2 for paper, or 3 for scissors: "))
	if player_input == 1:
		player_1 = "Rock"
		break
	elif player_input == 2:
		player_1 = "Paper"
		break
	elif player_input == 3:
		player_1 = "Scissors"
	else:
		print("Enter either 1, 2, or 3")

print("Player 1 has chosen "+player_1)
player_2 = random.choice(["Rock","Paper","Scissors"])
print("Player 2 has chosen "+player_2)

if player_1 == player_2:
	winner = "Neither"
elif player_1 == "Rock" and player_2 == "Scissors":
	winner = "Player 1"
elif player_1 =="Paper" and player_2 == "Rock":
	winner = "Player 1"
elif player_1 == "Scissors" and player_2 == "Paper":
	winner = "Player 1"
else:
	winner = "Player 2"
print("The winner is "+winner)