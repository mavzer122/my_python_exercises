from random import randint
def guess_game():
	guesses = 1
	random_number = randint(1, 9)
	while True:
		user_guess = raw_input("Please enter a number between 1 and 9. Type exit to quit. ")
		if user_guess == "exit":
			break
		elif int(user_guess) == random_number:
			print "You guessed correctly!"
			print "You have guessed " + str(guesses) + " times."
			break
		elif int(user_guess) < random_number:
			print "Too low!"
			guesses += 1
		elif int(user_guess) > random_number:
			print "Too high!"
			guesses += 1
		else:
			continue
		
		
guess_game()
