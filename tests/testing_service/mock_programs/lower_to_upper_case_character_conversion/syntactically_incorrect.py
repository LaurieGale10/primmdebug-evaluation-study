def convert_to_uppercase(lowercase)
	asciiValue = ord(lowercase)
	if asciiValue < 97 or asciiValue > 122:
		return "You did not input a lowercase letter"
	else:
		newAsciiValue = asciiValue - 32
		newCharacter = chr(newAsciiValue)
		return newCharacter

lowercaseCharacter = input("Enter lowercase character: ")
newCharacter = convert_to_uppercase(lowercaseCharacter)
print("The uppercase version of",lowercaseCharacter,"is",newCharacter)