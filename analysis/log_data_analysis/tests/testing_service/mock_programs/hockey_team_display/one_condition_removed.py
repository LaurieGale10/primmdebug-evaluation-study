country1 = input("Enter the name of the first country: ")
country2 = input("Enter the name of the second country: ")

if len(country1) < 6 or country1.startswith('C'):
	shortened_country1 = country1[:2]
else:
	shortened_country1 = country1[:3]


print("Team 1:", shortened_country1)
print("Team 2:", country2[:2])