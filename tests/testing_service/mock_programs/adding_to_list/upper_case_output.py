list = [5, 7, 12]
print("INITIAL LIST:", list)
user_input = int(input("Please enter an integer: "))
list.append(user_input)
list.sort()
print("UPDATED LIST:", list)