list = [5, 7, 12]
print("Initial list:", list)
user_input = int(input("Please enter an integer: "))
list.append(user_input)
list.sort()
print("Updated list:", list)