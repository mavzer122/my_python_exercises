from random import randint

a = []
for items in range(20):
	a.append(randint(1, 999))
print sorted(a)
b = [items for items in a if items % 2 == 0]
print sorted(b)
#the below does the same as line 7 but with more readable code
#for items in a:
	#if items % 2 == 0:
		#b.append(items)
#print b
