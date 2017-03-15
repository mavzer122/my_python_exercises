import random
print '''Welcome to my Rock, Paper, Scissors game.
You will play 3 times against the computer.'''

def rock_paper_scissors():
	a = ["Rock", "Paper", "Scissors"]
	plays = 0
	while plays <= 2:
		plays += 1
		user_input = raw_input("Type Rock, Paper or Scissors: ")
		computer_choice = random.choice(a)
		if user_input == computer_choice:
			print "Tie Game!"
			print "The computer chose " + computer_choice
		elif user_input == "Rock" and computer_choice == "Paper":
			print "You lose!"
			print "The computer chose " + computer_choice
		elif user_input == "Rock" and computer_choice == "Scissors":
			print "Congrats! You win!"
			print "The computer chose " + computer_choice
		elif user_input == "Paper" and computer_choice == "Rock":
			print "Congrats! You win!"
			print "The computer chose " + computer_choice
		elif user_input == "Paper" and computer_choice == "Scissors":
			print "You lose!"
			print "The computer chose " + computer_choice
		elif user_input == "Scissors" and computer_choice == "Rock":
			print "You lose!"
			print "The computer chose " + computer_choice
		elif user_input == "Scissors" and computer_choice == "Paper":
			print "Congrats! You win!"
			print "The computer chose " + computer_choice
		else:
			print "Please enter 'Rock', 'Paper' or 'Scissors'"
			plays -= 1

rock_paper_scissors()
while True:
	play_again = raw_input("Type Yes to play again, type Quit to exit. ")
	if play_again == "Yes":
		rock_paper_scissors()
	elif play_again == "Quit":
		break
