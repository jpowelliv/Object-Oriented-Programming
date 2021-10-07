#Joseph E. Powell IV
#11.14.18
#CIS 225 car.py/ driver.py

class Car():

    def __init__(self, make, model, year):
        self.make = make
        slef.model = model
        self.wheels = 4
        self.year = year
        odometerRead = 0.0

    def getMake(self):
        return self.make

    def getOdometerRead():
        return odometerRead

    def _str_(self):
        return self.make + "(" + self.model + ") " + self.year

def main():
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    odometerRead = float(input("Enter Odometer reading: "))
    print()
    print("What's the mileage ")
    print("TIME TO PUSH IT TO THE LIMIT!!! BBBAAAABBBBBYYYYY!!")

main()
    
    
