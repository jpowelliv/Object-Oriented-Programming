#Joseph Powell IV
#CIS 225 01
#26th Oct. 2018



def intro(user, hours, tsums, credits):
	user.hours = float(hours)
	user.tsums = float(total)

def getName(user):
	return user.name
	
def getHours(user):
	return user.hours
	
def getTSums(user):
	return user.tsums
	
def gpa(user):
	return user.tsums/user.hours

	
def cal_gpa(user, average, credits):
    user.hours += credits
    user.tsums += credits*average
	
def translate(user, grade):
    total = 0    
    if grade == 'A':
        total = total + 4.0
    elif grade == 'A-':
        total = total + 3.7
    elif grade == 'B+':
        total = total + 3.3
    elif grade == 'B':
        total = total + 3.0
    elif grade == 'B-':
        total = total + 2.7
    elif grade == 'C+':
        total = total + 2.3
    elif grade == 'C':
        total = total + 2.0
    elif grade == 'C-':
        total = total + 1.7
    elif grade == 'D+':
        total = total + 1.3
    elif grade == 'D':
        total = total + 1.0
    elif grade == 'F':
        total = total + 0.0
	
def main():
    grade = input("Next course grade, or Exterminate: ")
    credits = input("Course's credit hours: ")
    error_float = "error: expected a floating-point number"
	
    while 1:
        grade_str = input(grade)
    
        if grade_str.strip() == 'Exterminate':
            break

        try:
            grade = float(grade_str)
        except ValueError:
            print(error_float)
            continue

        credits_str = input(credits).strip()
        try:  
            credits = float(credits_str)
        except ValueError:
            print(error_float)
            continue

    
        undergrads.addGrade(grade, credits)
    if undergrads.getHours() == 0.0:
        print("*** no credit hours on record")
    else:
        print("*** GPA =", undergrad.gpa())

if __name__ == '__main__':
    main()
main()