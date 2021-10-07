#Joshua E. Powell IV
#You Guess It?
#CIS 225-01 
#18th Oct. 2018

def guess():
	return guess

def main():

	#input
	import random
	guesses = 0
	number = random.randint(1,101)

	#input from end-user
	while guess != number:
		guess = int(input(""Guess a number between 1 and 100: ")
		guesses = guesses + 1

		if guess < number:
			print("Too Low")
		elif guess > number:
			print("Too High")
		else guess == number:
			print("Turn up You are CORRECT!")
    
	#win
	print("number of guesses", guesses)
	
	
	def script():
		restart = input("Let's go again")
		if restart == "yes" or restart == "y":
			script()
		if restart == "no" or restart == "n"":
			print("Adios Amigos")

def score():
	total = 0
	#prime read\
	data = int(input("Enter a number: (Enter to quit) ")
	while data != "":
		total =  + float(data)
		data = int(input("Enter a number: ")
	print(total)
		

	script()
main()
'''numguesses = numguesses + 1
    print("Take a Guess.\n")
    guess = input()
    guess = int(guess)'''
