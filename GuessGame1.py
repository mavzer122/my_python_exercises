from random import randint
def guess_game():
	guesses = 1
	random_number = randint(1, 9)
	while True:
		user_guess = raw_input("Please enter a number between 1 and 9. Type exit to quit. ")
		if user_guess == "exit":
			break
		try:
			user_guess = int(user_guess)
		except:
			print "That's not a number."
			continue
		if int(user_guess) > 9 or int(user_guess) < 1:
			print "You should enter a number between 1 and 9."
		elif int(user_guess) == random_number:
			print "You guessed correctly!"
			print "You have found the number in " + str(guesses) + " guesses."
			random_number = randint(1, 9)
			guesses -= guesses
		elif int(user_guess) < random_number:
			print "Too low!"
			guesses += 1
		elif int(user_guess) > random_number:
			print "Too high!"
			guesses += 1
		else:
			continue
		
		
guess_game()
