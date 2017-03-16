####PASSWORD GENERATOR####
import random
import sys


password_components = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
		'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
		'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
		'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '_', '#', '-', '?']
		
#I had to do this otherwise it raises an error when a large number is entered,
#...because random.sample does not allow repetition
#...and I simply couldn't find any other method to do this
password_components = password_components * 999
print "Welcome to Password Generator v0.1. You may type 'exit' to quit."
def generatePassword():
	while True:
		password_length = raw_input("Write in integers how long you want your password to be. ")
		if password_length == "exit":
			break
		try:
			password_length = int(password_length)
		except:
			print "That's not an integer!"
			continue
		password_complete = random.sample(password_components, int(password_length))
		for item in password_complete:
			sys.stdout.write(item)
		print ""
		

generatePassword()
