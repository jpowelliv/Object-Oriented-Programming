#Joseph Powell IV
#09/04/18
#Convert Liters to Gallons

def main():

	print("Convert Liters to Gallons Chart")
	print("L...Gal")
	for i in range(10):
			liters = i + 1
			gallons = (liters * 3.78541)
			print(liters, "...", gallons)
			
main()