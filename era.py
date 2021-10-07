#Joseph Powell
#CIS 225-01
#10/02/18

def era_cal(runs, inns):
	
    era = (runs * 9) / inns
    return era

def main():

    name = input("Player's name: ")
    inns = int(input("Number of innings?: "))
    runs = int(input("Number of runs?: "))

    answer = era_cal(runs, inns)
    print(name, "ERA is", answer)

    num_str = input("Number of pitchers on roster: ")
    num = int(num_str)