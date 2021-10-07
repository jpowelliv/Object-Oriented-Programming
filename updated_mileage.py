#Joseph Powell IV
#CIS 225-01
#31th October 2018

def get_data():
    starting_odometer = float(input("The starting mileage on odometer: "))
    gallons = float(input("Amount of gallons pumped from station: "))
    ending_odometer = float(input("The ending milage on odeometer: "))
    return get_data
	
	try get_data():
	except:
		return 0, 0, 0

def calculate_mpg(get_data):
    miles = (end_odometer - starting_odometer)
    try:
        mpg = miles / gallons
    except:
        return 0
    return mpg

def display(mpg):
    print("Mileage is", mpg)
	starting_odometer, ending_odometer, gallons = get_data()
    mpg = calculate_mpg(starting_odometer, ending_odometer, gallons)
    display (mpg)

def main():
    starting_odometer, ending_odometer, gallons = get_data()
    mpg = calculate_mpg(starting_odometer, ending_odometer, gallons)
    display (mpg)

main()