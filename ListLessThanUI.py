from random import randint
a = []
for random_integer in range(20):
	a.append(randint(0, 999))
user_input = raw_input('Please enter a number. > ')
b = [item for item in a if item <= int(user_input)]
print sorted(b)
#for item in a:
	#if item <= int(user_input):
		#b.append(item)
		#print b
