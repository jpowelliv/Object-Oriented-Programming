#Joseph Powell
#CIS 225-01
#9/25/18

#encode to words
def main():
	
	message = input("What are we encoding?: ")

	#loop
	for letter in message:
		ch = chr(ord(letter)+1)
		print(ch end=" ")
		
main()


'''
#encode to numbers
def main():
	
	message = input("Enter the message to encode")

	#loop
	for letter in message:
		ch = (ord(letter)+1)
		print(ch, end=" ")
		
main()'''


