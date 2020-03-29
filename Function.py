def Say_hello(name):
	print("Hello",name)

print(Say_hello("Shivam"))

###########################


def dog_check(mystring):
	if 'dog' in mystring.lower():
		return True
	else:
		return False

print(dog_check('My Dog Ran Away'))
print(dog_check('My Cat Ran Away'))
##############################################
def dog_chec(mystring):
	return 'dog' in mystring.lower()								

print(dog_chec('My Dog Ran Away'))

###########################################

def add(x,y):
	return x+y

print(add(5,10))

#########################################
def pig_latin(word):
	first_letter  = word[0]
	if first_letter in 'aeiou':
		pig_word = word + 'ay'
	else:
		pig_word = word[1:]+ first_letter + 'ay'

	return pig_word

print(pig_latin("apple"))
print(pig_latin("shivam"))
