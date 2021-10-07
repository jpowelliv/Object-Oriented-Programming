#Joseph Powell IV
#CIS 225-01
#24th Oct. 2018


sum = 0
students = 0
while True:
    GPA = eval(input("Students GPAs are(To quit Enter 0): "))
    if GPA == 0:
        break
    students = students + 1
    sum = sum + GPA

def main():
    average = sum / students
    print("GPA average is: ", round(average, 2))
    print("Students surveyed is: ", students)

main()
