name = raw_input("What's your name? > ")
age = raw_input("How old are you? > ")

print "Hello " + name + " you're " + age + " years old."
age_in_100_years = int(age) + 100
age_sentence = "You will turn " + str(age_in_100_years) + " in 100 years.\n"
print age_sentence
numbers = raw_input("Could you enter a number please? > ")
print age_sentence * int(numbers)
