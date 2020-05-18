def check_winner(numbers, winner):
	draw = 0
	if numbers[0] == numbers[1] == numbers[2] == "O" or numbers[0] == numbers[3] == numbers[6] == "O" or numbers[0] == numbers[4] == numbers[8] == "O" or numbers[2] == numbers[5] == numbers[8] == "O" or numbers[3] == numbers[4] == numbers[5] == "O" or numbers[1] == numbers[4] == numbers[7] == "O" or numbers[6] == numbers[7] == numbers[8] == "O" or numbers[0] == numbers [2] == numbers[6] == "O":
		print("player O is the winner!")
		winner = True	
		return winner
	elif numbers[0] == numbers[1] == numbers[2] == "X" or numbers[0] == numbers[3] == numbers[6] == "X" or numbers[0] == numbers[4] == numbers[8] == "X" or numbers[2] == numbers[5] == numbers[8] == "X" or numbers[3] == numbers[4] == numbers[5] == "X" or numbers[1] == numbers[4] == numbers[7] == "X" or numbers[6] == numbers[7] == numbers[8] == "X" or numbers[0] == numbers [2] == numbers[6] == "X":			
		print("player X is the winner!")
		winner = True
		return winner
	elif winner == False:
		for symbols in numbers:
			if symbols != " ":
				draw += 1
		if draw == 9:
			print("Draw")
			winner = True
			return winner
		else:
			return winner						

def play_round(numbers):
	O = 0
	X = 0
	player_input = int(input("Give me a positional number 1 - 9 starting at the top left: "))
	i = player_input - 1
	if numbers[i] == " ":
		for symbols in numbers:
			if symbols == "X":
				X += 1
			elif symbols == "O":
				O += 1
		if X == O:
			numbers[i] = "X"
			return numbers
		elif O < X:
			numbers[i] = "O"
			return numbers
	else:
		print("Please enter an empty slot")
		play_round(numbers)	
	
def display_grid(numbers):
	if numbers == [" ", " ", " ", " ", " ", " ", " ", " ", " "]:
		print("""	
		_|_|_
		_|_|_
		 | |			
		""")
	else:
		print(f"""	
		{numbers[0]}|{numbers[1]}|{numbers[2]}
		{numbers[3]}|{numbers[4]}|{numbers[5]}
		{numbers[6]}|{numbers[7]}|{numbers[8]}			
		""")

def start():
	winner = False
	numbers = [" " for space in range(9)]
	display_grid(numbers)
	while winner == False:
		numbers = play_round(numbers)
		display_grid(numbers)
		winner = check_winner(numbers, winner)
	if winner == True:
		again = input("Play again? y/n: ")
		if again == "y":
			start()
		else:
			print("Thanks for playing!")

start()
