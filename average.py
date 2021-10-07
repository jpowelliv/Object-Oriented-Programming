#Joseph Powell IV
#CIS 225-01
#09/06/18
#Average.py

def main():
	print("Average Number Calculator")
	print()
	
	n = int(input("How many numbers you would like to add?"))
	sum = 0
	for i in range(n):
		value = int(input("Enter the next number: "))
		print(value)
		
		sum = (sum + value)
		mean = int(sum / n)
	print(mean)
	
main()