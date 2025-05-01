user_answer = input("What is the capital of Hungary? ").lower()

# Display the user's answer
print("You answered:",user_answer)

# Check if the answer is correct and display the appropriate message
if user_answer == "budapest":
	print("Correct!")
else:
	print("Incorrect. The correct answer is Budapest.")