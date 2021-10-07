#Joseph Powell
#CIS 225-01
#9/25/18


#decode to words
def main():
	
    message = input("Lets decode! ")

    #loop
    for letter in message:
        ch = chr(ord(letter)-1)
        print(ch, end=" ")
		
main()


'''#decode to numbers
def main():

    message = input("Enter the message to decode: ")
    myList = message.split()
	
	#loop
    for item in myList:
        num = (int(item)-1)

        print(chr(num), end="")
	
main()'''