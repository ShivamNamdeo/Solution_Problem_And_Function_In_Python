print("Ques1 : Sam Print only the words that start with s in this sentence ")

str = "Sam Print only the words that start with s in this sentence"

for word in str.split():
	if word[0].lower() =='s':
		print(word)

print("###############An Another Way#################")
################################

for word in str.split():
	if word[0] ==('s' or 'S'):
		print(word)

print("Ques 2 : Use range() to print all the even numbers from 0 to 10")

print('''for num in range(0,11,2):
	print(num,end=" ")''')

for num in range(0,11,2):
	print(num,end=" ")

print("############An Another Way##################")
print("list(range(0,11,2))")
print(list(range(0,11,2)))
print("############An Another Way##################")
print("[num for num in range(0,11,2)]")
print([num for num in range(0,11,2)])
print("############An Another Way##################")
print("[num for num in range(0,11) if num%2==0]")
print([num for num in range(0,11) if num%2==0])

print("Ques 3 :Use a list comprehension to create a list of all numbers between 1 and 50 that are divisible by 3")
print("[num for num in range(1,51) if num %3==0]")
print([num for num in range(1,51) if num %3==0])

print("Ques 4 : print every word in this sentence that has an even number of letters")
str = "print every word in this sentence that has an even number of letters"
print("[word for word in str.split() if len(word)%2==0]")
print([word for word in str.split() if len(word)%2==0])

print('''Ques 5 : write a program that prints the integers from 1 to 100 .but multiplies of 3 print
	"Fizz" instead of the number ,and for the multiplies of 5 print "Buzz" ,for 
	multiplies of both print "FizzBuzz"''')
for num in range(1,101):
	if num%3==0:
		print("Fizz",num,end =" ")
	if num%5==0:
		print("Buzz",num,end =" ")
	if (num%3==0 and num%5==0):
		print("Fizz Buzz",num,end =" ")

print("######An Another Way##############")
for num in range(1,101):
	if  (num%3==0 and num%5==0):
		print("FizzBuzz")
	elif num%3==0:
		print("Fizz")
	elif num%5==0:
		print("Buzz")
	else:
		print(num)


print("Create a list of the first letters of every word on this string")
str = "Create a list of the first letters of every word on this string"

print([word[0] for word in str.split()])