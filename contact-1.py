#Joseph Powell
#CIS 225-01
#contacts/py





def main():

	
	n = int(input("How many people are in your contact list? \n"))
	contacts = []
	n = 3
	
	#loop
	for i in range(n):
			
		#get user's first and lastnames 
		first = input("Please enter your first name (all lowercase): ")
		last = input("Please enter your last name (all lowercase): ")
		contact = str(i + 1) + "." + " " +last + "," + first
		print(i)
		contacts,append(contact)
		
	
	#second loop
	contacts = ["Ben", "Annd", "Jerry"]
	for contact in contacts:
		#output
		print("Contacts is", contact)
	
main()