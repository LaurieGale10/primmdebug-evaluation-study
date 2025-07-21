count=1
multiple = int(input("Input the number that you would like to find the times table of: "))
print("The first 12 multiples of the number",multiple," are:")
while count<=12:
	times_table = multiple * count
	count=count+1
	print(times_table)