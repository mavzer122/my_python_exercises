number1 = raw_input('Please enter a number to check if it is even or odd. \n> ')

if int(number1) % 2 != 0:
	print number1 + " is an odd number."
elif int(number1) % 4 == 0:
	print number1 + " is divisible by 4, therefore is an even number."
else:
	print number1 + " is an even number."

