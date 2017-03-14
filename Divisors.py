user_number = raw_input("Please enter a number between 1 and 9999.\n > ")
list_of_divisors = []
for element in range(1,999):
	if int(user_number) % element == 0:
		list_of_divisors.append(element)
		print list_of_divisors
