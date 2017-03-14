from random import randint

a = []
b = []
c = []
for random_ints in range(50):
	a.append(randint(1, 999))
print a
for random_ints in range(50):
	b.append(randint(1, 999))
print b
for element in a:
	if element in b:
		c.append(element)
		print c
