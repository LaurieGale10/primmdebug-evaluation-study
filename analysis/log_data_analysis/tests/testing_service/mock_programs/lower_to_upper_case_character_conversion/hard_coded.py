def convert_to_uppercase(lowercase):
	asciiValue = ord(lowercase)
	if asciiValue < 97 or asciiValue > 122:
		return "You did not input a lowercase letter"
	else:
		if lowercase == "w":
			return "W"

lowercaseCharacter = input("Enter lowercase character: ")
newCharacter = convert_to_uppercase(lowercaseCharacter)
print("The uppercase version of",lowercaseCharacter,"is",newCharacter)