#Break : Break out of current closest enclosing loop
#Continue : Goes to the top of the closest enclosing loop
#Does nthing at all

x = [1,2,3]
for i in x:
	pass
	#Not Use Then Error
	#Pass The Error

print("-------------------")
str = "Sammy"
for letter in str:
	print(letter)


print("-------------------")
for letter in str:
	if letter == "a":
		continue
	print(letter)

print("-------------------")
for letter in str:
	if letter == "a":
		break
	print(letter)

print("-------------------")
for letter in str:
	if letter == "a":
		continue
	print(letter)

print("-------------------")

