# Define the secret colour and number
secret_colour = "blue"
secret_number = 42

# Start by prompting the user for their choice
choice = input("Enter 'A' to guess the secret colour or 'B' to guess the secret number: ")

if choice == 'A':
	# Guess the secret colour
	color_guess = ""
	while colour_guess != secret_colour:
		colour_guess = input("Guess the secret colour: ")
		if colour_guess == secret_colour:
			print("Correct! The secret colour is blue.")
		else:
			print("Incorrect! Try again.")

elif choice == 'B':
	# Guess the secret number
	number_guess = 0
	while number_guess != secret_number:
		try:
			number_guess = int(input("Guess the secret number: "))
			if number_guess == secret_number:
				print("Correct! The secret number is 42.")
			else:
				print("Incorrect! Try again.")
		except ValueError:
			print("Please enter a valid number.")

else:
	# If the user enters an invalid choice
	print("Invalid choice. Please restart the program and enter 'A' or 'B'.")
	
print("Program finished!")